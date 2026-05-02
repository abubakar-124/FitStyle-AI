# 👕 FitStyle AI

> **AI-powered size & outfit recommendations based on your body measurements**

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange?style=flat-square)
![HuggingFace](https://img.shields.io/badge/Hosted%20on-Hugging%20Face-yellow?style=flat-square&logo=huggingface)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📌 About

**FitStyle AI** is a smart fashion assistant that takes your body measurements and style preferences, then instantly recommends the perfect outfit, clothing size, and color palette — all through a clean, modern web interface.

No sign-up. No complicated setup. Just enter your measurements and get results.

---

## ✨ Features

- 📐 **Smart Size Detection** — Calculates your clothing size (S / M / L / XL) from height and waist
- 👤 **Body Type Analysis** — Identifies your build (Slim / Average / Broad) with a visual reference image
- 👕 **Outfit Recommendations** — Suggests complete outfits for Casual, Formal, and Streetwear styles
- 🎨 **Color Palette Tips** — Recommends colors that suit your body type and chosen style
- 🚻 **Gender-Aware** — Separate recommendations for Male and Female
- 🖼️ **Visual Output** — Shows body type and outfit suggestion images side by side
- 🌙 **Dark Theme UI** — Modern dark gradient interface built with Gradio

---

## 🖥️ Demo

🔗 **Live App:** [Try it on Hugging Face Spaces](https://huggingface.co/spaces/YOUR_USERNAME/fitstyle-ai)

| Your Measurements | Your Style Profile |
|---|---|
| Enter height, waist, gender & style | Get size, build, outfit & color tips |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/fitstyle-ai.git
cd fitstyle-ai

# 2. Install dependencies
pip install gradio

# 3. Run the app
python app.py
```

The app will launch at `http://localhost:7860` in your browser.

---

## 📁 Project Structure

```
fitstyle-ai/
│
├── app.py                  # Main application file
│
├── slim.jpg.jpeg           # Male slim body image
├── medium.jpg.jpeg         # Male medium body image
├── heavy.jpg.jpeg          # Male heavy body image
├── casual.jpg.jpeg         # Male casual outfit image
├── formal.jpg.jpeg         # Male formal outfit image
├── streetwear.jpg.jpeg     # Male streetwear outfit image
│
├── female slim.jpg.jpeg    # Female slim body image
├── female medium.jpg.jpeg  # Female medium body image
├── female heavy.jpg.jpeg   # Female heavy body image
├── female casual.jpg.jpeg  # Female casual outfit image
├── female formal.jpg.jpeg  # Female formal outfit image
├── female streetwear.jpg.jpeg  # Female streetwear outfit image
│
└── README.md
```

---

## 🧠 How It Works

1. **User inputs** height (cm), waist size (cm), gender, and preferred style
2. **Size logic** maps waist measurements to clothing sizes:
   - Waist < 71 cm → **Small (S)** — Slim / Athletic build
   - Waist 71–85 cm → **Medium (M)** — Average / Regular build
   - Waist ≥ 86 cm → **Large (L) / XL** — Broad / Plus build
3. **Outfit engine** selects outfit, image, and color palette based on chosen style
4. **Results** are displayed as a formatted profile with two reference images

---

## 🎨 Style Options

| Style | Outfit | Colors |
|-------|--------|--------|
| **Casual** | Tee + Slim-fit Jeans + Sneakers | Olive, Beige, Navy |
| **Formal** | Dress Shirt + Tailored Trousers + Derby Shoes | White, Charcoal, Navy |
| **Streetwear** | Graphic Hoodie + Cargo Joggers + High-tops | Black/White, Monochrome, Red |

---

## 🛠️ Built With

- **[Python](https://www.python.org/)** — Core logic
- **[Gradio](https://gradio.app/)** — Web UI framework
- **[Hugging Face Spaces](https://huggingface.co/spaces)** — Deployment platform

---

## 📦 Deployment on Hugging Face

1. Create a new Space on [huggingface.co/spaces](https://huggingface.co/spaces)
2. Select **Gradio** as the SDK
3. Upload `app.py` and all image files
4. The Space will automatically build and deploy

---

## 🤝 Contributers

Zeeshan
Fatima Shahid
Aleeha Kashaf
Youmna saifulah
Dua Rajper

---
## Running Application

https://huggingface.co/spaces/Abubakar763/FitStyle-Ai

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---


⭐ If you found this useful, give it a star on GitHub!
