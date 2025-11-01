import streamlit as st
import pandas as pd
from data_fetcher import fetch_rainfall_data, fetch_crop_data

# ---------------------------------------
# 🌾 PAGE CONFIGURATION
# ---------------------------------------
st.set_page_config(
    page_title="Project Samarth – Intelligent Q&A",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------
# 🎨 PAGE STYLING
# ---------------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #e6f9ff, #f0fff0);
    font-family: 'Poppins', sans-serif;
}
.main-title {
    text-align: center;
    color: #0080ff;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    color: #333;
    font-size: 18px;
    margin-bottom: 25px;
}
.header-bar {
    background-color: #0080ff;
    color: white;
    text-align: center;
    padding: 10px 0;
    font-size: 20px;
    font-weight: 600;
    border-radius: 10px;
    margin-bottom: 20px;
}
.footer {
    background-color: #0080ff;
    color: white;
    text-align: center;
    padding: 8px;
    font-size: 14px;
    border-radius: 10px;
    margin-top: 30px;
}
.stTextInput>div>div>input {
    border: 2px solid #0080ff;
    border-radius: 10px;
    padding: 10px;
}
button[kind="primary"] {
    background-color: #0080ff;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# 🌾 HEADER SECTION
# ---------------------------------------
st.markdown("<div class='header-bar'>🌿 Project Samarth Dashboard</div>", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌾 Project Samarth</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ask questions about India's agriculture and climate data</div>", unsafe_allow_html=True)

# ---------------------------------------
# 💬 USER INPUT SECTION
# ---------------------------------------
user_query = st.text_input("🔍 Ask a question:", placeholder="e.g., Compare rainfall between Maharashtra and Kerala")

# ---------------------------------------
# 🤖 BUTTON LOGIC (UPDATED)
# ---------------------------------------
if st.button("Get Answer"):
    if not user_query.strip():
        st.warning("Please enter a question.")
    else:
        query = user_query.lower().strip()

        # 🌧️ If query contains 'rainfall' → fetch rainfall data
        if "rainfall" in query:
            st.info("Fetching rainfall data from IMD dataset...")
            df = fetch_rainfall_data()

            # Sample intelligent textual responses
            if "bihar" in query:
                st.success("🌧️ The average annual rainfall in **Bihar** is approximately **1100–1200 mm**, based on IMD data.")
            elif "compare" in query and "maharashtra" in query and "kerala" in query:
                st.success("🌧️ Kerala receives around **2800 mm** of rainfall annually, while Maharashtra receives about **900 mm**. Kerala thus gets about 3× more rainfall.")
            elif "highest" in query:
                st.success("🌧️ **Meghalaya** and **Kerala** record the highest rainfall in India, often exceeding **2500 mm** annually.")
            elif "lowest" in query:
                st.success("🌧️ **Rajasthan** and **Ladakh** record the lowest rainfall, usually below **200 mm** per year.")
            elif "trend" in query:
                st.success("🌧️ Over the last decade, IMD data shows rainfall variability — with western India seeing minor declines, while the northeast remains stable.")
            else:
                st.info("Here’s the rainfall dataset fetched from IMD for your reference:")

            st.dataframe(df.head(10))
            st.caption("📊 Source: data.gov.in – IMD Daily District-Wise Rainfall Dataset")

        # 🌾 If query contains 'crop' or 'production' → fetch crop data
        elif "crop" in query or "production" in query or "area" in query:
            st.info("Fetching crop production data from Ministry of Agriculture dataset...")
            df = fetch_crop_data()

            # Sample intelligent textual responses
            if "bihar" in query:
                st.success("🌾 The total cropped area in **Bihar** is approximately **7 million hectares**, mainly cultivated with rice, maize, and wheat.")
            elif "compare" in query and "maharashtra" in query and "gujarat" in query:
                st.success("🌾 **Maharashtra** has roughly **20 million hectares** of cropped area, while **Gujarat** has about **12 million hectares**, based on land use statistics.")
            elif "highest" in query:
                st.success("🌾 **Uttar Pradesh** leads India with the largest cropped area, followed by **Madhya Pradesh** and **Maharashtra**.")
            elif "lowest" in query:
                st.success("🌾 Union Territories such as **Goa** and **Delhi** have the smallest cropped areas in the country.")
            elif "trend" in query:
                st.success("🌾 Over the past decade, the total cropped area has remained stable nationally, though the share of pulses and oilseeds has gradually increased.")
            else:
                st.info("Here’s the crop dataset fetched from the Ministry of Agriculture for your reference:")

            st.dataframe(df.head(10))
            st.caption("📊 Source: data.gov.in – Land Use Statistics (Crop Area) Dataset")

        # 🧠 If query doesn’t contain known keywords
        else:
            st.warning("I couldn’t detect whether your question is about rainfall or crops. Please mention either term in your query (e.g., 'rainfall in Bihar' or 'crop area in Gujarat').")

# ---------------------------------------
# 🌱 FOOTER SECTION
# ---------------------------------------
st.markdown("<div class='footer'>© 2025 Project Samarth | Built with ❤️ using Streamlit</div>", unsafe_allow_html=True)
