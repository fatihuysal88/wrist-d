# models
- 20 deep learning-based object detection models
- Proposed WFD ensemble models
# i) transfer learning with MMDetection
- DCN
- Dynamic R-CNN
- Faster R-CNN
- FSAF
- Libra R-CNN
- PAA
- RetinaNet
- RegNet
- SABL
# ii) Proposed WFD ensemble models
- WFD-1 (RegNet, FSAF, RetinaNet, SABL RetinaNet, PAA), (1, 5, 5, 5, 5)
- WFD-2 (DCN, SABL Faster R-CNN), (2, 2)
- WFD-3 (RegNet, PAA, FSAF, Libra RetinaNet), (3, 3, 3, 4)
- WFD-4 (RegNet, PAA, FSAF, SABL RetinaNet), (1, 3, 3, 1)
- WFD-5 (FSAF, Faster R-CNN, DCN, Lİbra RetinaNet, RetinaNet), (2, 1, 4, 2, 3)
- WFD-C (WFD-1, WFD-3, WFD-4, WFD-5, WFD-2), (4, 4, 3, 5, 5)
