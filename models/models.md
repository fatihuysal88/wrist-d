# models
- 20 deep learning-based object detection models
- Proposed WFD ensemble models
# i) transfer learning with MMDetection
- DCNv2 (Faster R-CNN) with ResNet50 Bacbone Network
- Dynamic R-CNN with ResNet50 Bacbone Network
- Faster R-CNN with ResNet50 Bacbone Network
- FSAF with ResNet50 Bacbone Network
- Libra R-CNN (RetinaNet) with ResNet50 Bacbone Network
- PAA with ResNet50 Bacbone Network
- RetinaNet with ResNet50 Bacbone Network
- RegNet (RetinaNet) with RegNetX-3.2GF Bacbone Network
- SABL (Faster R-CNN and RetinaNet) with ResNet50 Bacbone Network
# ii) Proposed WFD ensemble models
- WFD-1 (RegNet, FSAF, RetinaNet, SABL RetinaNet, PAA), (1, 5, 5, 5, 5)
- WFD-2 (DCN, SABL Faster R-CNN), (2, 2)
- WFD-3 (RegNet, PAA, FSAF, Libra RetinaNet), (3, 3, 3, 4)
- WFD-4 (RegNet, PAA, FSAF, SABL RetinaNet), (1, 3, 3, 1)
- WFD-5 (FSAF, Faster R-CNN, DCN, Lİbra RetinaNet, RetinaNet), (2, 1, 4, 2, 3)
- WFD-C (WFD-1, WFD-3, WFD-4, WFD-5, WFD-2), (4, 4, 3, 5, 5)
