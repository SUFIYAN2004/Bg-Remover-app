# 🪄 Bg Remover App with Streamlit

This project is a simple and powerful web app that removes the background from any image using Python, Streamlit, and the `rembg` library.

## 🎯 Features

- Upload an image through a clean UI
- Automatically remove its background using AI (ONNX + rembg)
- Download the background-removed image
- Error handling for unsupported image formats
- Auto-create `original/` folder to store uploads

## 🚀 Tech Stack

- **Python**
- **Streamlit** – UI framework
- **rembg** – AI-powered background removal
- **PIL (Pillow)** – Image handling
- **io**, **os** – File operations

## 📦 Setup Instructions

1. **Clone the repo:**
```bash
git clone https://github.com/YOUR_USERNAME/Bg-Remover-app.git
cd Bg-Remover-app

Create & activate virtual environment (Windows)
python -m venv env
env\Scripts\activate

Install dependencies:
pip install -r requirements.txt
Run the app
streamlit run remove_bg_app.py

📁 Folder Structure
Bg-Remover-app/
├── env/                 # Virtual environment (ignored)
├── original/            # Uploaded images (ignored)
├── remove_bg_app.py     # Main app script
├── requirements.txt     # Dependencies
└── README.md            # This file

🔒 .gitignore
Your .gitignore excludes:
env/
original/
__pycache__/
.DS_Store

📺 Watch the video tutorial:
🎥 YouTube: https://www.youtube.com/@SufLearning

🧠 Credits
Created with ❤️ by SufLearning
Subscribe for more Python mini projects!


---

✅ After saving `README.md`, run this in terminal to add and push:

```bash
git add README.md
git commit -m "Add detailed project README"
git push
