# Ai-quality-control
Ai based defect detection using open cv and yolo
AI Quality Control System
Overview

This project is a prototype AI-assisted quality control system designed to demonstrate real-time object detection and inspection using computer vision. It integrates OpenCV, YOLO (Ultralytics), and Flask to stream live camera footage to a web-based dashboard and display AI predictions in real time.

The system represents Phase-1 of an industrial AI quality inspection pipeline, focusing on pre-trained object detection and material identification, rather than defect classification using factory-specific datasets.

Features

# Live webcam feed using OpenCV

# Real-time object detection with YOLOv8

# Web-based dashboard using Flask & HTML/CSS

# Bounding boxes and confidence scores rendered on video

# Acts as a pseudo-prototype for industrial quality control systems
Requirements

Tech Stack

Python

OpenCV

YOLOv8 (Ultralytics)

Flask

HTML / CSS / JavaScript

System Architecture

OpenCV captures live video frames from the webcam

YOLOv8 performs object detection on each frame

Bounding boxes and labels are drawn on frames

Flask streams the processed frames to the browser

The dashboard displays live AI predictions
