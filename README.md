# 🌿 Smart Irrigation System using AI (Edunet - AICTE Internship)

![Smart Irrigation Logo](assets/logo.jpg)

## 🔍 Overview
This project automates irrigation using machine learning, soil moisture sensors, and weather conditions. It predicts whether each sprinkler in a farm plot should be ON or OFF, improving water usage efficiency.

> 🚀 Internship: Smart Automated Irrigation using Soil Moisture & Weather Data  
> 👨‍🏫 Mentor: Mr. Raghunandan M S  
> 👨‍💻 Intern: Dilli Prasanna Bandi  

---

## 💧 System Architecture

<img src="assets/flow-diagram-of-the-irrigation-system copy.png" alt="Smart Irrigation Flowchart" width="700"/>

---

## 📊 Features

- 🌱 Uses 20 environmental and soil-based sensors.
- 🤖 Predicts ON/OFF status using a trained ML model (`RandomForestClassifier` with `MultiOutputClassifier`).
- 📈 Visual dashboard built with **Streamlit**.
- 💾 Model serialized with **joblib** (`Farm_Irrigation_System.pkl`).
- 🖼️ Project sections: Overview, Methodology, Enhancements, and Contact.

---

## 📂 Project Structure

Smart_Irrigation/
├── app.py # Main Streamlit Dashboard
├── Farm_Irrigation_System.pkl # Trained ML model
├── assets/
│ ├── logo.jpg # Project Logo
│ └── flow-diagram.png # System Architecture Diagram
├── requirements.txt # Dependencies
└── README.md # Project Overview

---


---

## 🧠 Tech Stack

| Component      | Tools                         |
|----------------|-------------------------------|
| Language        | Python                        |
| ML Model        | Random Forest (Scikit-learn)  |
| UI              | Streamlit                     |
| Deployment      | GitHub + Streamlit Share      |
| Visualization   | Matplotlib / Plotly           |
| Version Control | Git, GitHub                   |

---

## 🚀 Future Enhancements

- 📡 **Add real-time weather API**  
  Integrate current weather data to improve irrigation predictions.
- 📲 **Mobile app interface**  
  Control and monitor sprinklers from mobile devices.
- ☁️ **Cloud-based IoT integration**  
  Enable real-time data syncing from sensors using IoT platforms.
- 📊 **Live dashboard analytics**  
  Track sensor trends, predictions, and water usage over time.

---

## 📌 Why Smart Irrigation?

- ✅ **Reduces water wastage** by automating irrigation timing.
- ✅ **Minimizes human error** through smart predictions.
- ✅ **Efficient for large-scale farming** with 20+ sensors supported.
- ✅ **Aligns with sustainable agriculture & UN SDGs**.

---

## 🙌 Acknowledgements

This project is part of the **Edunet Foundation's AICTE Green Skills Internship**, powered by **Shell**.  
Special thanks to the mentors, organizers, and all contributors.

---

## 📬 Contact

If you'd like to connect or collaborate, reach out via:  
📧 Email: *bandidilliprasanna19@gmail.com*  
🔗 LinkedIn:www.linkedin.com/in/dilliprasannabandi



---




