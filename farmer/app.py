import streamlit as st
import google.generativeai as genai
from PIL import Image

# Yahan apni Google Gemini API Key dalein
genai.configure(api_key="AQ.Ab8RN6I58ZkPC2EYRi0WOrs2ue7USiEoMjwx3gZNG_HgvE64Og")

# Gemini 1.5 Flash model select karein (jo image aur text dono samajhta hai)
model = genai.GenerativeModel('gemini-3.5-flash')

# Website ka Title
st.title("Bhatia Krishi Mitr")
st.write("Farming product ki photo upload karein aur uski puri jankari payein.")

# User se input lene ke liye fields
product_name = st.text_input("Fertilizer/Pesticide ka naam (agar pata ho):")
uploaded_file = st.file_uploader("Product ki photo upload karein", type=["jpg", "png", "jpeg"])

# Submit Button
if st.button("Jankari Nikaalein"):
    if uploaded_file is not None:
        # Photo show karein
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        st.write("⏳ AI Jankari nikaal raha hai, kripya pratiksha karein...")
        
        # AI ke liye System Prompt
        prompt = f"""
        Aap ek expert agronomist (agriculture scientist) hain. 
        Product ka naam: {product_name}. 
        Niche di gayi photo ko dhyan se dekhein aur Hindi mein yeh details dein:
        1. Yeh product kya kaam aata hai?
        2. Yeh kin fasalon ke liye best hai?
        3. Alag-alag mitti (Retili, Chikni, etc.) ke hisaab se iski kitni matra (dosage) use karni chahiye?
        4. Ise spray karte waqt kya savdhaniyan rakhni chahiye?
        """
        
        # AI ko photo aur prompt bhejein
        response = model.generate_content([prompt, image])
        
        # Result website par show karein
        st.success("✅ Jankari mil gayi!")
        st.markdown(response.text)
    else:
        st.warning("⚠️ Kripya pehle ek photo upload karein.")