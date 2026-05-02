import gradio as gr
import os

def safe_image(path):
    return path if os.path.exists(path) else None

def fitstyle_ai(height, waist, gender, style):
    if waist is None or height is None:
        return "⚠️ Please enter Height and Waist.", None, None

    prefix = "female " if gender == "Female" else ""

    if waist < 25:
        size      = "Small (S)"
        body_img  = f"{prefix}slim.jpg.jpeg"
        body_note = "Slim / Athletic build"
    elif waist < 35:
        size      = "Medium (M)"
        body_img  = f"{prefix}medium.jpg.jpeg"
        body_note = "Average / Regular build"
    else:
        size      = "Large (L) / XL"
        body_img  = f"{prefix}heavy.jpg.jpeg"
        body_note = "Broad / Plus build"

    if style == "Casual":
        outfit     = "Classic Tee + Slim-fit Jeans + Sneakers"
        outfit_img = f"{prefix}casual.jpg.jpeg"
        color_tip  = "Earthy tones — olive, beige, navy"
    elif style == "Formal":
        outfit     = "Fitted Dress Shirt + Tailored Trousers + Derby Shoes"
        outfit_img = f"{prefix}formal.jpg.jpeg"
        color_tip  = "Neutral tones — white, charcoal, navy"
    else:
        outfit     = "Graphic Hoodie + Cargo Joggers + High-top Sneakers"
        outfit_img = f"{prefix}streetwear.jpg.jpeg"
        color_tip  = "Bold combos — black/white, monochrome, pops of red"

    result = f"""
### 👤 Body Profile
- Height: {height} cm
- Waist: {waist} cm
- Gender: {gender}
- Size: **{size}**
- Build: {body_note}
---
### 👕 Outfit Recommendation
- Outfit: **{outfit}**
- Colors: {color_tip}
"""
    return result, safe_image(body_img), safe_image(outfit_img)

CSS = """
body, .gradio-container {
    background: linear-gradient(135deg, #0F0C29, #1a1a2e, #16213E) !important;
    font-family: 'Segoe UI', sans-serif !important;
    color: #FFFFFF !important;
}
 
.gradio-container h1 {
    text-align: center !important;
    background: linear-gradient(90deg, #FB923C, #FBBF24) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
}
 
.gradio-container h2,
.gradio-container h3,
.gradio-container h4 {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    font-weight: 700 !important;
}
 
.gradio-container p,
.gradio-container li {
    color: #E5E7EB !important;
    -webkit-text-fill-color: #E5E7EB !important;
}
 
.gradio-container label > span {
    color: #CBD5E1 !important;
    -webkit-text-fill-color: #CBD5E1 !important;
    font-weight: 500 !important;
}
 
.gradio-container .block,
.gradio-container .form,
.gradio-container fieldset {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 14px !important;
}
 
.gradio-container input[type="number"],
.gradio-container input[type="text"] {
    background: #0f1b2d !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border-radius: 8px !important;
}
 
.gradio-container .gradio-radio label,
.gradio-container .gradio-checkboxgroup label,
.gradio-container [data-testid="radio-group"] label,
.gradio-container .wrap > label,
.gradio-container .radio-item,
.gradio-container .gradio-radio > div,
.gradio-container .selection {
    background: #1a1a2e !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 8px !important;
    color: #FBBF24 !important;
    -webkit-text-fill-color: #FBBF24 !important;
    font-weight: 500 !important;
}
 
.gradio-container button.primary {
    background: linear-gradient(135deg, #FB923C, #F97316) !important;
    border-radius: 12px !important;
    font-weight: bold !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border: none !important;
    font-size: 1rem !important;
}
"""

with gr.Blocks(css=CSS) as app:
    gr.Markdown("# 👕 FitStyle AI")
    gr.Markdown("AI-powered size & outfit recommendations")

    with gr.Row():
        with gr.Column():
            gr.Markdown("## 📐 Your Measurements")
            height_in = gr.Number(label="Height (cm)")
            waist_in  = gr.Number(label="Waist Size (cm)")
            gender_in = gr.Radio(["Male", "Female"], label="Gender")
            style_in  = gr.Radio(["Casual", "Formal", "Streetwear"], label="Select Style")
            submit_btn = gr.Button("✨ Generate Result", variant="primary")

        with gr.Column():
            gr.Markdown("## ✨ Your Style Profile")
            result_out = gr.Markdown()
            with gr.Row():
                body_img   = gr.Image(label="Body Type", height=220)
                outfit_img = gr.Image(label="Outfit Suggestion", height=220)

    submit_btn.click(
        fn=fitstyle_ai,
        inputs=[height_in, waist_in, gender_in, style_in],
        outputs=[result_out, body_img, outfit_img]
    )

app.launch()