#  Deepfake Detection with FastAPI & PyTorch

A full-stack project that detects deepfake images using a Convolutional Neural Network (CNN) trained with PyTorch and served via a FastAPI backend. Upload an image, and the system will tell you whether it's *Real* or *Fake*.

---

##  Features

- 🔍 Deepfake detection using a trained PyTorch CNN model  
- ⚡ FastAPI-powered backend for real-time inference  
- 📁 Supports image upload and classification via API  
- 🔄 CORS enabled — plug into any frontend app  
- 🧠 Easy-to-integrate detection module using detect.py

---

##  Tech Stack

- 🐍 Python 3.8+
- 🔥 PyTorch
- ⚙ FastAPI
- 🎨 PIL (Pillow)
- 🧪 Torchvision
- 🌐 CORS Middleware

---

##  Project Structure
<pre>
DeepfakeDetection/
├── backend/
│   ├── app.py                 # FastAPI application entry point
│   ├── utils/
│   │   └── detect.py          # Deepfake detection logic using PyTorch model
│   ├── models/
│   │   └── deepfake_model.pth # Pretrained CNN model for deepfake classification
│   └── uploads/               # Folder for temporarily saving uploaded images
</pre>
## How to Run the Server

✅ 1. Install Requirements
pip install fastapi uvicorn python-multipart torch torchvision pillow
✅ 2. Start the Server
Option 1 (Recommended):
uvicorn app:app --reload
Model Info
deepfake_model.pth: Trained CNN-based model saved in the models/ folder.

The model is loaded at startup and used in utils/detect.py.

## 📝 Notes
Ensure models/deepfake_model.pth exists relative to backend/.

The server saves uploaded images temporarily in the uploads/ folder.

Add .gitignore if you're using Git to avoid uploading large model or image file
## How It Works
The model is a lightweight CNN trained on real and deepfake images. It takes a 224x224 input image, processes it through convolutional layers, and outputs a probability score to classify the image.


## Future Improvements
 Use Transfer Learning with pretrained XceptionNet or EfficientNet

 Add support for deepfake video frames

 Build a React-based frontend UI

 Deploy on Render/Heroku/Vercel with CI/CD

## 🤝 Contributing
Contributions are welcome! Please open issues and submit pull requests for improvements or bug fixes.

📬 Contact
Siddharth Parmar<br/>
<a href="https://www.linkedin.com/in/siddharth-parmar-1245b4240?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">LinkedIn</a><br/> 
Siddharth.official.swe@gmail.com
