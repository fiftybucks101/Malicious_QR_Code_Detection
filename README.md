# 📲 **Malicious URL Detection in QR Codes** 🔍✨

---

## 🌟 **Project Overview** 🔲

🚀 This project unveils a **Malicious QR Code Detector** to evaluate QR code safety!  
🔧 **How it works**: Extracts the URL hidden in a QR code and uses an **Artificial Neural Network (ANN)** to classify it as:  
- ✅ **Safe**  
- ❌ **Unsafe**  

🛡️ By analyzing URLs, it guards against threats like **phishing**, **malware**, and other nasty surprises tied to shady QR codes.  
🎯 **Goal**: Deliver a trusty, efficient tool to tackle risks in our QR code-powered world!

---

## 📊 **Data Collection** 💾

🌐 **Source**: Kaggle dataset packed with safe and malicious URLs.  
📈 **Stats**:  
- Total: **654,132 URLs**  
- Original Split: **70% Safe** (~457,892) | **30% Malicious** (~196,240)  
- After Downsampling: **50/50 Balanced Ratio** ⚖️  

🧹 **Preprocessing**: Downsampling applied to even out the classes, boosting ANN accuracy and fairness across safe and unsafe predictions.

---

## 🎥 **Project Demo**  
![Demo](real_gif.gif)  
*See it in action!*

---


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

