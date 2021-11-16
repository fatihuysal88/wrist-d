# wrist-d
<p align="left">
  
<a>[![LICENSE](https://img.shields.io/github/license/fatihuysal88/wrist-d.svg)](https://github.com/fatihuysal88/wrist-d/blob/master/LICENSE)</a>
<a href="https://www.mdpi.com/journal/diagnostics/special_issues/Computer-Aided_Diagnosis">
    <img src="https://img.shields.io/badge/paper-under review-blue"/></a>
<a href="https://doi.org/10.3390/app11062723">
    <img src="https://img.shields.io/badge/arxiv-preprint-green"/></a>
</p>

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/fracture-detection-in-wrist-x-ray-images/medical-object-detection-on-gazi-university)](https://paperswithcode.com/sota/medical-object-detection-on-gazi-university?p=fracture-detection-in-wrist-x-ray-images)  
PyTorch Implementation for Fracture Detection in Wrist Bone X-ray Images
# note:
**Paper**: Under Review at MPDI Diagnostics  

**Submission Date**: November 12, 2021  
# abstract
Wrist fractures are common cases in hospitals, particularly in emergency services. Physicians need images from various medical devices, and patient’s medical history and physical examination to diagnose these fractures correctly and apply proper treatment. This study aims to perform fracture detection using deep-learning on wrist X-ray images to assist physicians not specialized in the field, working in emergency services in particular, in diagnosis of fractures. For this purpose, 20 different detection procedures were performed using deep learning-based object detection models on dataset of wrist X-ray images obtained from Gazi University Hospital. DCN, Dynamic R-CNN, Faster R-CNN, FSAF, Libra R-CNN, PAA, RetinaNet, RegNet and SABL deep learning-based object detection models with various backbones were used herein. To further improve detection procedures in the study, 5 different ensemble models were developed, which were later used to reform an ensemble model to develop a detection model unique to our study, titled ‘wrist fracture detection-combo (WFD-C)’. Based on detection of 26 different fractures in total, the highest result of detection was 0.8639 average precision (AP50) in WFD-C model developed. This study is supported by Huawei Turkey R&D Center within the scope of the ongoing cooperation project coded 071813 among Gazi University, Huawei and Medskor.  

**Keywords**: artificial intelligence; biomedical image processing; bone fractures; deep learning; fracture detection; object detection; transfer learning; wrist; X-ray  
# paper links
**Paper**: Under Review at MPDI Diagnostics  

**Preprint**: https://arxiv.org/abs/2111.07355  

**Papers With Code**: https://paperswithcode.com/paper/fracture-detection-in-wrist-x-ray-images  

**GitHub**: https://github.com/fatihuysal88/wrist-d  
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
  
