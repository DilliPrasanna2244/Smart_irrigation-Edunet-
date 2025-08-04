import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("Farm_Irrigation_System.pkl")

# Page configuration
st.set_page_config(page_title="Smart Irrigation", layout="wide")

# Custom CSS for dark theme and grey dashboard panel
# Dark theme and font fix
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: white;
        font-family: 'Segoe UI', sans-serif;
        font-size: 16px;
    }
    .main {
        background-color: #1c1c1c;
        padding: 20px;
        border-radius: 10px;
    }
    .css-18e3th9 {
        background-color: #2f2f2f !important;
    }
    .stSlider > div {
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 8px;
    }
    .sidebar .sidebar-content {
        font-size: 16px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar image
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4817/4817661.png", width=200)

# Sidebar title and description
st.sidebar.title("🌿 Smart Irrigation")
st.sidebar.markdown("""
**Project:** Smart Automated Irrigation using Soil Moisture & Weather Data  
**Mentor:** Raghunandan M S  
**Internship:** This internship is presented by Edunet Foundation in collaboration with AICTE & Shell, focusing on Green Skills using AI technologies.  
**Objective:** To automate irrigation systems using machine learning for efficient water usage.  

---

### 🔍 Sections  
- Dashboard  
- Why Smart Irrigation?  
- Methodology  
- Future Enhancements  
- Contact  
""")


# --- Tabs Layout ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Dashboard",
    "🌿 Why Smart Irrigation?",
    "⚙️ Methodology",
    "🚀 Future Enhancements",
    "📚 References & Contact"
])

# ==================== TAB 1: DASHBOARD ====================
with tab1:
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.title("💧 Smart Sprinkler Prediction System")

    st.markdown("""
    Enter sensor values between 0 and 1 (scaled) to predict sprinkler ON/OFF status.  
    This model controls 20 smart sprinklers based on environmental and soil conditions.
    """)

    sensor_values = []
    st.markdown("### 🔧 Sensor Input Panel")
    cols = st.columns(2)
    for i in range(20):
        col = cols[i % 2]
        val = col.slider(f"Sensor {i+1}", 0.0, 1.0, 0.5, 0.01)
        sensor_values.append(val)

    if st.button("🌱 Predict Sprinklers"):
        input_array = np.array(sensor_values).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        on_count = np.sum(prediction)

        st.success(f"**{on_count} out of 20 sprinklers will be ON.**")
        st.markdown("### 🔍 Sprinkler Status")
        spr_cols = st.columns(4)
        for i, status in enumerate(prediction):
            icon = "💡" if status == 1 else "❌"
            color = "green" if status == 1 else "red"
            spr_cols[i % 4].markdown(
                f"<div style='color:{color}; font-weight:bold;'>Parcel {i+1}: {icon} {'ON' if status==1 else 'OFF'}</div>",
                unsafe_allow_html=True
            )
    st.markdown("</div>", unsafe_allow_html=True)

# ==================== TAB 2: WHY SMART IRRIGATION ====================
with tab2:
    st.header("🌿 Why Smart Irrigation?")
    st.markdown("""
- 💧 **Water Conservation:** Prevents overwatering and saves precious water resources.
- 🚜 **Automated Monitoring:** Eliminates manual checks, saving time and labor.
- 🌱 **Healthier Crops:** Maintains optimal moisture for better yields.
- 🌦️ **Weather Adaptation:** Can adapt irrigation needs based on weather.
- 📉 **Cost Efficiency:** Reduces electricity, labor, and maintenance costs.
    """)

# ==================== TAB 3: METHODOLOGY ====================
with tab3:
    st.header("⚙️ Methodology")
    st.markdown("### 📊 Workflow Overview:")
    st.markdown("""
1. **Data Collection:** Gather soil moisture & environmental sensor data  
2. **Preprocessing:** Normalize values using `MinMaxScaler`  
3. **Model Training:** Use `RandomForestClassifier` inside `MultiOutputClassifier`  
4. **Deployment:** Save with `joblib`, deploy with Streamlit  
5. **Prediction:** Model returns ON/OFF for each sprinkler  
    """)

    st.markdown("### 🧰 Tools & Stack:")
    st.markdown("""
- Python, Streamlit  
- Scikit-learn  
- NumPy, Pandas  
- Joblib for model storage  
- GitHub for version control  
    """)

# ==================== TAB 4: FUTURE ENHANCEMENTS ====================
with tab4:
    st.header("🚀 Future Enhancements")
    st.markdown("""
- 📡 **Weather API Integration:** Real-time rainfall, humidity, temperature  
- 🔌 **IoT Hardware:** Raspberry Pi or Arduino with real sensors  
- 📱 **Mobile App Dashboard:** Remote control and alerts  
- 📊 **Analytics Panel:** Graphs on water saved, daily activity  
- 🧠 **Advanced ML Models:** XGBoost, LightGBM, Deep Learning  
    """)

# ==================== TAB 5: REFERENCES & CONTACT ====================
with tab5:
    st.header("📚 References")
    st.markdown("""
- 🧠 **Model:** Random Forest with MultiOutputClassifier  
- 📁 **Data Source:** Simulated/Real sensor data  
- 🎓 **Internship:** AICTE Green Skill by Edunet Foundation """) 
    
    st.header("Contact")
    st.markdown("""
- 💻 **GitHub Repo:** https://github.com/DilliPrasanna2244/Smart_irrigation-Edunet-.git  
- 📧 **Email:**bandidilliprasanna19@gmail.com  
    """)
