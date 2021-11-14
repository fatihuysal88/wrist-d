import cv2
import os
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
from skimage.filters import farid_h
from skimage.io import imread


class custom_Dataset:

    def __init__(self, source_dir="./source/", target_dir="./target/", resize_dim=800):  # get initialize data

        check_source_dir = os.path.isdir(source_dir)
        check_target_dir = os.path.isdir(target_dir)
        # If folders doesn't exist, then create it.
        if not check_source_dir:
            os.makedirs(source_dir)
            print("Created Folder :source")
        if not check_target_dir:
            os.makedirs(target_dir)
            print("Created Folder :target")

        self.source_dir = source_dir  # define source folder path
        self.target_dir = target_dir  # define target folder path
        self.resize_dim = resize_dim  # resize paramater set 800 as default

    def cluster(self, image):
        """
           Apply clustering algorithm for change background if image has more white pixel
           :param numpy.ndarray image: 3-channel image
           """
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # read image with opencv
        reshape = image.reshape((image.shape[0] * image.shape[1], 3))
        cluster = KMeans(n_clusters=2).fit(reshape)  # apply cluster algorithm with n=2

        labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
        (hist, _) = np.histogram(cluster.labels_, bins=labels)
        hist = hist.astype("float")
        hist /= hist.sum()
        colors = sorted([(percent, color) for (percent, color) in zip(hist, cluster.cluster_centers_)], reverse=True)
        _max_color = []
        _max_percent = 0
        for (percent, color) in colors:
            if percent > _max_percent:
                _max_percent = percent
                _max_color = color
        return _max_color[0]

    def background(self, source, target):
        for filename in os.listdir(source):
            img = cv2.imread(os.path.join(source, filename))
            _max_color = self.cluster(self, img)
            if _max_color > 110:
                img = 255 - img
            new_path = target + filename
            old_path = source + "/" + filename
            os.remove(old_path)
            cv2.imwrite(new_path, img)

    def applyClahe(self):
        """
                   Apply Clahe algorithm with clipLimit=7.0, tileGridSize=(11, 11)
                   """
        for filename in os.listdir(self.target_dir):
            image = cv2.imread(os.path.join(self.target_dir, filename), 0)  # read image from directory
            clahe = cv2.createCLAHE(clipLimit=7.0, tileGridSize=(11, 11))  # determine clahe values great
            img = clahe.apply(image)  # apply clahe transform on image
            new_path = self.target_dir + filename  # determine new path for save to image
            cv2.imwrite(new_path, img)  # save output to new paths

    def imageResize(self):
        for filename in os.listdir(self.source_dir):
            image = Image.open(os.path.join(self.source_dir, filename))
            image.thumbnail((800, 800))
            r = filename.replace(" ", "")
            new_path = self.target_dir + r  # determine new path for save to image
            image.save(new_path)
            image.close()
            os.remove(os.path.join(self.source_dir, filename))

    def runPreProcess(self):
        self.imageResize()
        self.applyClahe()


if __name__ == '__main__':
    custom_Dataset.background()
