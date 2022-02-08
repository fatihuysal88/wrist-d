# wrist-d
<p align="left">
  
<a>[![LICENSE](https://img.shields.io/github/license/fatihuysal88/wrist-d.svg)](https://github.com/fatihuysal88/wrist-d/blob/master/LICENSE)</a>
<a href="https://www.mdpi.com/1424-8220/22/3/1285">
    <img src="https://img.shields.io/badge/paper-published-blue"/></a>
<a href="https://arxiv.org/abs/2111.07355">
    <img src="https://img.shields.io/badge/arxiv-preprint-green"/></a>
</p>

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/fracture-detection-in-wrist-x-ray-images/medical-object-detection-on-gazi-university)](https://paperswithcode.com/sota/medical-object-detection-on-gazi-university?p=fracture-detection-in-wrist-x-ray-images)  
PyTorch Implementation for Fracture Detection in Wrist X-ray Images
# note:
**Published**: 8 February 2022, Hardalaç, F.; Uysal, F.; Peker, O.; Çiçeklidağ, M.; Tolunay, T.; Tokgöz, N.; Kutbay, U.; Demirciler, B.; Mert, F. Fracture Detection in Wrist X-ray Images Using Deep Learning-Based Object Detection Models. Sensors 2022, 22, 1285. https://doi.org/10.3390/s22031285 IF 2020: 3.576, Index: SCIE, JCR: Q1, EF: x.yz, AI: x.yz  
# abstract
Hospitals, especially their emergency services, receive a high number of wrist fracture cases. For correct diagnosis and proper treatment of these, images obtained from various medical equipment must be viewed by physicians, along with the patient’s medical records and physical examination. The aim of this study is to perform fracture detection by use of deep-learning on wrist X-ray images to support physicians in the diagnosis of these fractures, particularly in the emergency services. Using SABL, RegNet, RetinaNet, PAA, Libra R-CNN, FSAF, Faster R-CNN, Dynamic R-CNN and DCN deep-learning-based object detection models with various backbones, 20 different fracture detection procedures were performed on Gazi University Hospital’s dataset of wrist X-ray images. To further improve these procedures, five different ensemble models were developed and then used to reform an ensemble model to develop a unique detection model, ‘wrist fracture detection-combo (WFD-C).’ From 26 different models for fracture detection, the highest detection result obtained was 0.8639 average precision (AP50) in the WFD-C model. Huawei Turkey R&D Center supports this study within the scope of the ongoing cooperation project coded 071813 between Gazi University, Huawei and Medskor.  

**Keywords**: artificial intelligence; biomedical image processing; bone fractures; deep learning; fracture detection; object detection; transfer learning; wrist; X-ray  
# paper links
**Paper**: https://www.mdpi.com/1424-8220/22/3/1285  

**Preprint**: https://arxiv.org/abs/2111.07355  

**Papers With Code**: https://paperswithcode.com/paper/fracture-detection-in-wrist-x-ray-images  

**GitHub**: https://github.com/fatihuysal88/wrist-d  
# citation
please cite the paper if you benefit from our paper:  
```
@Article{s22031285,
AUTHOR = {Hardalaç, Fırat and Uysal, Fatih and Peker, Ozan and Çiçeklidağ, Murat and Tolunay, Tolga and Tokgöz, Nil and Kutbay, Uğurhan and Demirciler, Boran and Mert, Fatih},
TITLE = {Fracture Detection in Wrist X-ray Images Using Deep Learning-Based Object Detection Models},
JOURNAL = {Sensors},
VOLUME = {22},
YEAR = {2022},
NUMBER = {3},
ARTICLE-NUMBER = {1285},
URL = {https://www.mdpi.com/1424-8220/22/3/1285},
ISSN = {1424-8220},
ABSTRACT = {Hospitals, especially their emergency services, receive a high number of wrist fracture cases. For correct diagnosis and proper treatment of these, images obtained from various medical equipment must be viewed by physicians, along with the patient&rsquo;s medical records and physical examination. The aim of this study is to perform fracture detection by use of deep-learning on wrist X-ray images to support physicians in the diagnosis of these fractures, particularly in the emergency services. Using SABL, RegNet, RetinaNet, PAA, Libra R-CNN, FSAF, Faster R-CNN, Dynamic R-CNN and DCN deep-learning-based object detection models with various backbones, 20 different fracture detection procedures were performed on Gazi University Hospital&rsquo;s dataset of wrist X-ray images. To further improve these procedures, five different ensemble models were developed and then used to reform an ensemble model to develop a unique detection model, &lsquo;wrist fracture detection-combo (WFD-C).&rsquo; From 26 different models for fracture detection, the highest detection result obtained was 0.8639 average precision (AP50) in the WFD-C model. Huawei Turkey R&amp;D Center supports this study within the scope of the ongoing cooperation project coded 071813 between Gazi University, Huawei and Medskor.},
DOI = {10.3390/s22031285}
}
```
# authors
* **Fırat HARDALAÇ** - [Prof. at Gazi University, Republic of Turkey.](https://orcid.org/0000-0003-1358-0756)
* **Fatih UYSAL** - [PhD Candidate and Research Assistant at Gazi University, Republic of Turkey.](https://orcid.org/0000-0002-1731-2647)
* **Ozan PEKER** - [MSc student at Gazi University, Republic of Turkey.](https://orcid.org/0000-0003-2258-1531)
* **Murat ÇİÇEKLİDAĞ** - [Research Assistant at Gazi University, Republic of Turkey.](https://orcid.org/0000-0001-7883-9445)
* **Tolga TOLUNAY** - [Assoc. Prof. at Gazi University, Republic of Turkey.](https://orcid.org/0000-0003-1998-3695)
* **Nil TOKGÖZ** - [Prof. at Gazi University, Republic of Turkey.](https://orcid.org/0000-0003-2812-1528)
* **Uğurhan KUTBAY** - [Assoc. Prof. at Gazi University, Republic of Turkey.](https://orcid.org/0000-0003-2167-9107)
* **Boran DEMİRCİLER** - [R&D Manager at Huawei Turkey.](https://orcid.org/)
* **Fatih MERT** - [R&D Manager at Huawei Turkey.](https://orcid.org/0000-0002-2896-5475)
# proposed detection models
![models](https://github.com/fatihuysal88/wrist-d/blob/main/docs/figs/proposed%20detection%20models.png)
# proposed ensemble models
![models](https://github.com/fatihuysal88/wrist-d/blob/main/docs/figs/proposed%20ensemble%20models.png)
# model performance
![models](https://github.com/fatihuysal88/wrist-d/blob/main/docs/figs/ensemble%20models%20performance.PNG)
# sample of wrist fracture results
![models](https://github.com/fatihuysal88/wrist-d/blob/main/docs/figs/sample%20of%20wrist%20fracture%20results.PNG)

**Note**: ground-truth bounding box (green), predicted bounding box (red)  

# requirements
  
<a href="https://github.com/open-mmlab/mmdetection">
  <img align="center" style="margin:1rem 0.5rem" src="https://github-readme-stats.vercel.app/api/pin/?username=open-mmlab&repo=mmdetection&title_color=ffffff&text_color=c9cacc&icon_color=4AB197&bg_color=1A2B34" width="350" height="180"/><a 
  href="https://github.com/kemaloksuz/LRP-Error">
  <img align="center" style="margin:1rem 0.5rem" src="https://github-readme-stats.vercel.app/api/pin/?username=kemaloksuz&repo=LRP-Error&title_color=ffffff&text_color=c9cacc&icon_color=4AB197&bg_color=1A2B34" width="350" height="180"/>
  <a href="https://github.com/rafaelpadilla/review_object_detection_metrics">
  <img align="center" style="margin:1rem 0.5rem" src="https://github-readme-stats.vercel.app/api/pin/?username=rafaelpadilla&repo=review_object_detection_metrics&title_color=ffffff&text_color=c9cacc&icon_color=4AB197&bg_color=1A2B34" width="350" height="180"/><a 
  href="https://github.com/albumentations-team/albumentations">
  <img align="center" style="margin:1rem 0.5rem" src="https://github-readme-stats.vercel.app/api/pin/?username=albumentations-team&repo=albumentations&title_color=ffffff&text_color=c9cacc&icon_color=4AB197&bg_color=1A2B34" width="350" height="180"/>      
  <a href="https://github.com/ppwwyyxx/cocoapi">
  <img align="center" style="margin:1rem 0.5rem" src="https://github-readme-stats.vercel.app/api/pin/?username=ppwwyyxx&repo=cocoapi&title_color=ffffff&text_color=c9cacc&icon_color=4AB197&bg_color=1A2B34" width="350" height="180"/><a 
  href="https://github.com/pytorch/pytorch">
  <img align="center" style="margin:1rem 0.5rem" src="https://github-readme-stats.vercel.app/api/pin/?username=pytorch&repo=pytorch&title_color=ffffff&text_color=c9cacc&icon_color=4AB197&bg_color=1A2B34" width="350" height="180"/>
  <a href="https://github.com/ZFTurbo/Weighted-Boxes-Fusion">
  <img align="center" style="margin:1rem 0.5rem" src="https://github-readme-stats.vercel.app/api/pin/?username=ZFTurbo&repo=Weighted-Boxes-Fusion&title_color=ffffff&text_color=c9cacc&icon_color=4AB197&bg_color=1A2B34" width="350" height="150"/> 
  
