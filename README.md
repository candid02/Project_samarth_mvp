# 🌾 Project Samarth – Intelligent Q&A System on Indian Government Datasets
# Link:

👉 Open Project Samarth App

# If the app doesn’t load properly, please open the link in an incognito window to avoid Streamlit caching issues.

# 🚀 Overview

Project Samarth is an intelligent Q&A dashboard that connects directly to live datasets from data.gov.in
to provide real-time insights on India’s agriculture and climate data.
Users can ask natural language questions (like “Compare rainfall in Bihar and Kerala” or “Show total crop area for Maharashtra”) and get data-backed answers with source references.

# Vision

Government portals like data.gov.in hold thousands of valuable datasets released by different ministries.
However, these datasets are often inconsistent in structure and difficult to combine manually.

Project Samarth aims to solve this by creating a unified intelligent interface that:

Integrates data across ministries (Agriculture, IMD, etc.)

Answers natural language queries

Generates both summaries and tabular insights

Promotes data transparency and data-driven policymaking

# Example Questions (Try in the App!)

1️⃣ “Show rainfall data for Bihar.”
2️⃣ “Compare rainfall between Maharashtra and Kerala.”
3️⃣ “Total crop area in Tamil Nadu.”
4️⃣ “Show crop data for Bihar.”
5️⃣ “Which state has higher rainfall — Gujarat or Assam?”

Each query provides:

A short, human-readable summary

A data table preview

Source citation (IMD / Ministry of Agriculture)

# Future Improvements

Currently, the system uses two key datasets (Rainfall and Crop Area) for answering limited types of questions.
However, I plan to enhance the system further to:

🔍 Automatically detect question intent using NLP models

🧾 Dynamically fetch and merge multiple datasets from data.gov.in

💬 Provide direct, conversational answers for a wider range of questions

🧠 Add correlation analysis between rainfall and crop production trends

For now, you can try the example questions listed above, which fetch and visualize live data correctly.

# Datasets Used

# Rainfall Dataset
Source: India Meteorological Department (IMD)
API: State/District Wise Daily Rainfall Data – data.gov.in

# Crop Area Dataset
Source: Ministry of Agriculture & Farmers Welfare
API: Total Crop Area under Land Use Statistics – data.gov.in

# System Design

Architecture Overview:

User Query  →  Query Processor  →  Dataset Detection (Rainfall / Crop)
             →  Live API Fetch (data.gov.in)
             →  Data Cleaning + Summary Computation
             →  Answer Display (Text + Table)


# Core Features:

Average rainfall calculation by state
Total crop area computation by state
Basic reasoning and comparison summaries
Live API integration with IMD & Agriculture datasets


# Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	Python
Data Processing	Pandas, NumPy
API Access	requests
Visualization	Streamlit native tables
Hosting	Streamlit Cloud

# ⚙️ Setup Instructions (Run Locally)
# Clone this repository
git clone https://github.com/<your-username>/Project-Samarth.git
cd Project-Samarth

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
Then open the local URL displayed in your terminal.

# Conclusion

Project Samarth demonstrates how AI + Open Government Data can empower research, policymaking, and sustainability.
By connecting data across ministries, it transforms static datasets into actionable insights for India’s agriculture and climate economy.
