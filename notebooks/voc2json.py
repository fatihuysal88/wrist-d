import os
import glob
import xml.etree.ElementTree as ET
import json


class voc2json:
    def __init__(self, anno_path, json_path):
        self.anno_path = anno_path
        self.json_path = json_path
        self.START_BOUNDING_BOX_ID = 1
        self.PRE_DEFINE_CATEGORIES = None

    def get(self, root, name):
        vars = root.findall(name)
        return vars

    def get_and_check(self, root, name, length):
        vars = root.findall(name)
        if len(vars) == 0:
            raise ValueError("Can not find %s in %s." % (name, root.tag))
        if length > 0 and len(vars) != length:
            raise ValueError(
                "The size of %s is supposed to be %d, but is %d."
                % (name, length, len(vars))
            )
        if length == 1:
            vars = vars[0]
        return vars

    def get_filename_as_int(self, filename):
        try:
            filename = filename.replace("\\", "/")
            filename = os.path.splitext(os.path.basename(filename))[0]
            return str(filename)
        except:
            raise ValueError("Filename %s is supposed to be an integer." % filename)

    def get_categories(self, xml_files):

        classes_names = []
        for xml_file in xml_files:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for member in root.findall("object"):
                classes_names.append(member[0].text)
        classes_names = list(set(classes_names))
        classes_names.sort()

        return {name: i for i, name in enumerate(classes_names)}

    def convert(self, xml_files, json_file):
        json_dict = {"images": [], "type": "instances", "annotations": [], "categories": []}
        if self.PRE_DEFINE_CATEGORIES is not None:
            categories = self.PRE_DEFINE_CATEGORIES
        else:
            categories = self.get_categories(xml_files)
        bnd_id = self.START_BOUNDING_BOX_ID
        for xml_file in xml_files:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            path = self.get(root, "path")
            if len(path) == 1:
                filename = os.path.basename(path[0].text)
            elif len(path) == 0:
                filename = self.get_and_check(root, "filename", 1).text
            else:
                raise ValueError("%d paths found in %s" % (len(path), xml_file))
            # The filename must be a number
            image_id = self.get_filename_as_int(filename)
            size = self.get_and_check(root, "size", 1)
            width = int(self.get_and_check(size, "width", 1).text)
            height = int(self.get_and_check(size, "height", 1).text)
            image = {
                "file_name": os.path.basename(filename.replace("\\", "/")),
                "height": height,
                "width": width,
                "id": image_id,
            }
            json_dict["images"].append(image)
            for obj in self.get(root, "object"):
                category = self.get_and_check(obj, "name", 1).text
                if category not in categories:
                    new_id = len(categories)
                    categories[category] = new_id
                category_id = categories[category]
                bndbox = self.get_and_check(obj, "bndbox", 1)
                xmin = int(self.get_and_check(bndbox, "xmin", 1).text) - 1
                ymin = int(self.get_and_check(bndbox, "ymin", 1).text) - 1
                xmax = int(self.get_and_check(bndbox, "xmax", 1).text)
                ymax = int(self.get_and_check(bndbox, "ymax", 1).text)
                assert xmax > xmin
                assert ymax > ymin
                o_width = abs(xmax - xmin)
                o_height = abs(ymax - ymin)
                ann = {
                    "area": o_width * o_height,
                    "iscrowd": 0,
                    "image_id": image_id,
                    "bbox": [xmin, ymin, o_width, o_height],
                    "category_id": category_id,
                    "id": bnd_id,
                    "ignore": 0,
                    "segmentation": [],
                }
                json_dict["annotations"].append(ann)
                bnd_id = bnd_id + 1

        for cate, cid in categories.items():
            cat = {"supercategory": "none", "id": cid, "name": cate}
            json_dict["categories"].append(cat)
        json_fp = open("./ground_truth/" + json_file + str(".json"), "w")
        json_str = json.dumps(json_dict)
        json_fp.write(json_str)
        json_fp.close()

    def run(self):
        xml_files = glob.glob(os.path.join(self.anno_path, "*.xml"))
        self.convert(xml_files, self.json_path)
