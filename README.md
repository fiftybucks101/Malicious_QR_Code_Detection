# Malicious URL Detection In QR Code 

## Project Overview

This project introduces a Malicious QR Code Detector designed to assess the safety of QR codes. The system works by extracting the embedded URL from a QR code and leveraging an Artificial Neural Network (ANN) to classify it as either "safe" or "unsafe." By analyzing the URL, the detector aims to protect users from potential threats such as phishing, malware, or other malicious activities commonly associated with unsafe QR codes. The goal is to provide a reliable and efficient tool for identifying risks in an increasingly QR code-driven digital landscape.

## Data Collection

The dataset for this project was sourced from Kaggle, comprising a mix of safe and malicious URLs. It originally contained 654,132 URLs, with a 70/30 split favoring safe URLs (approximately 457,892 safe and 196,240 malicious). To ensure balanced training and improve model performance, downsampling was applied, reducing the dataset to an equal ratio of safe and malicious URLs. This preprocessing step mitigates bias toward the majority class and enhances the ANN's ability to generalize across both categories effectively.

## Project Demo
![alt text](real_gif.gif)


### dvc commands

1) git init
2) dvc init
3) dvc repro

- For metrics: dvc metrics show
- To see pipeline: dvc dag

### Project approach

1) Update config entity
2) Update Configuration Manager
3) Update Components
4) Create stages pipeline
5) Create dvc pipeline 

