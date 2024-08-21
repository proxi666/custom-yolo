# Custom YOLO Model for Rickshaw Detection

This repository contains a custom YOLO (You Only Look Once) model trained on a custom dataset for detecting cycle rickshaws. The dataset was annotated using the CVAT (Computer Vision Annotation Tool) and the model was trained using the Ultralytics YOLOv8 framework.

## Project Overview

The goal of this project is to accurately detect rickshaws in videos using a custom-trained YOLO model. The model has been trained with various data augmentation techniques to enhance its performance and robustness.

## Features

- **Model Training**: Trained using the YOLOv8 framework with extensive data augmentation.
- **Custom Dataset**: Annotated using CVAT for precise detection.
- **Video Inference**: The model is applied to videos to detect and highlight rickshaws in real-time.

## Analysis of YOLO Model

### Confusion Matrix

- **confusion_matrix.png**: The confusion matrix shows how well your model is performing in terms of correctly predicting the classes. For the class "cycle_rickshaw," the model correctly predicted 194 instances and made 1 incorrect prediction (false positive/negative). The model is performing very well, with only one misclassification.
  
- **confusion_matrix_normalized.png**: The normalized confusion matrix indicates the proportion of correct and incorrect classifications. Since both values for correct predictions are at 1.0, your model is highly accurate, correctly classifying the majority of the test instances.

### F1-Confidence Curve

- **F1_curve.png**: This curve demonstrates the relationship between the F1 score and the confidence threshold. A high and stable F1 score close to 1 across different confidence levels indicates that your model is both precise and has good recall across a range of confidence thresholds, making it a reliable model.

### Label Analysis

- **labels.jpg**: This plot helps visualize the distribution and positions of your labeled objects in the dataset. The majority of the "cycle_rickshaw" objects are distributed in a certain region of the image space, and the model may have learned to detect objects within those specific regions well.

- **labels_correlogram.jpg**: This correlogram shows the relationships between the labels in terms of their spatial characteristics, such as x, y, width, and height. This can provide insights into how your labeled data is structured and may help in understanding any biases or patterns in your dataset.

### Precision-Confidence Curve

- **P_curve.png**: This curve shows how the precision of the model varies with the confidence threshold. High precision indicates that when your model predicts a "cycle_rickshaw," it is usually correct. The curve suggests that your model maintains high precision across various confidence levels.

### Precision-Recall Curve

- **PR_curve.png**: The PR curve indicates the trade-off between precision and recall. A near-perfect curve, as seen here, indicates that your model is capable of maintaining high precision even when recall is high. This is a sign of a well-performing model.

### Recall-Confidence Curve

- **R_curve.png**: This curve shows the relationship between recall and the confidence threshold. High recall across confidence thresholds means that your model successfully identifies most of the true instances of "cycle_rickshaw" in your test set.

### Training and Validation Losses

- **results.png**: This plot shows the training and validation loss trends for bounding box regression, classification, and DFL (Distribution Focal Loss). The losses decrease steadily, indicating that the model is learning well over time. Additionally, the validation metrics, including precision, recall, and mAP (mean Average Precision), show improvement, which is a good sign that the model generalizes well to unseen data.

  


