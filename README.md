# Custom YOLO Model for Rickshaw Detection

This repository contains a custom YOLO (You Only Look Once) model trained on a custom dataset for detecting cycle rickshaws. The dataset was annotated using the CVAT (Computer Vision Annotation Tool) and the model was trained using the Ultralytics YOLOv8 framework.

## Project Overview

The goal of this project is to accurately detect rickshaws in videos using a custom-trained YOLO model. The model has been trained with various data augmentation techniques to enhance its performance and robustness.

## Features

- **Model Training**: Trained using the YOLOv8 framework with extensive data augmentation.
- **Custom Dataset**: Annotated using CVAT for precise detection.
- **Video Inference**: The model is applied to videos to detect and highlight rickshaws in real-time.

## Installation

To run this project, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV
- Ultralytics YOLOv8

You can install the required packages using pip:

```bash
pip install ultralytics opencv-python
