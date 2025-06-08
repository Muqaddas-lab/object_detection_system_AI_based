# YOLO Object Detection System

## Overview

This is a **real-time object detection system** using the YOLOv8 model with a user-friendly **Tkinter GUI** interface.  
You can select any video file, specify the class (object category) you want to detect, and start live detection with bounding boxes and confidence scores displayed on the video.

---

## Features

- Select any video file (.mp4 or others) for object detection.
- Input the class name to detect specific objects (e.g., person, car, dog).
- Real-time object tracking with bounding boxes.
- Unique colors assigned to different detected classes for better visualization.
- Start and stop detection buttons to control the process.
- Responsive and easy-to-use GUI using Tkinter.

---

## Libraries Used

- **Ultralytics YOLO**: For loading and running the YOLOv8 pre-trained model and object tracking.  
- **OpenCV**: For video processing and image manipulation.  
- **Pillow (PIL)**: For converting OpenCV images to a format compatible with Tkinter GUI.  
- **Tkinter**: To build the graphical user interface.

---

## Detectable Objects and Dataset

- The YOLOv8s model is pre-trained on the **COCO dataset** (Common Objects in Context).  
- It can detect **80 common object classes**, including but not limited to:

  - Person  
  - Bicycle  
  - Car  
  - Motorcycle  
  - Airplane  
  - Bus  
  - Train  
  - Truck  
  - Boat  
  - Traffic Light  
  - Fire Hydrant  
  - Stop Sign  
  - Parking Meter  
  - Bench  
  - Bird  
  - Cat  
  - Dog  
  - Horse  
  - Sheep  
  - Cow  
  - Elephant  
  - Bear  
  - Zebra  
  - Giraffe  
  - Backpack  
  - Umbrella  
  - Handbag  
  - Tie  
  - Suitcase  
  - Frisbee  
  - Skis  
  - Snowboard  
  - Sports Ball  
  - Kite  
  - Baseball Bat  
  - Baseball Glove  
  - Skateboard  
  - Surfboard  
  - Tennis Racket  
  - Bottle  
  - Wine Glass  
  - Cup  
  - Fork  
  - Knife  
  - Spoon  
  - Bowl  
  - Banana  
  - Apple  
  - Sandwich  
  - Orange  
  - Broccoli  
  - Carrot  
  - Hot Dog  
  - Pizza  
  - Donut  
  - Cake  
  - Chair  
  - Couch  
  - Potted Plant  
  - Bed  
  - Dining Table  
  - Toilet  
  - TV  
  - Laptop  
  - Mouse  
  - Remote  
  - Keyboard  
  - Cell Phone  
  - Microwave  
  - Oven  
  - Toaster  
  - Sink  
  - Refrigerator  
  - Book  
  - Clock  
  - Vase  
  - Scissors  
  - Teddy Bear  
  - Hair Drier  
  - Toothbrush  

---

## About YOLOv8 Model

- YOLO (You Only Look Once) is a popular **real-time object detection architecture** known for its speed and accuracy.  
- **YOLOv8** is the latest version from Ultralytics with improvements in detection quality, speed, and usability.  
- The model used here is **`yolov8s.pt`** (small version) which balances accuracy and speed, suitable for real-time applications.  
- The model supports both object detection and tracking.

  
