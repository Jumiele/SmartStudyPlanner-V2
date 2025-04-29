# 📘 Smart Study Planner V2

Smart Study Planner V2 is an updated, AI-powered web app that generates **personalized daily study plans** based on user input such as:

- Available study hours
- Subject difficulty
- Days remaining until exam
- Preferred learning style (Visual, Auditory, Kinesthetic)

This version improves on the original by integrating both:
- ✅ A machine learning model for structured study time allocation
- ✅ A Gemini-powered GenAI system for generating full motivational study plans


![image](https://github.com/user-attachments/assets/944c6aa2-3e80-499a-83cc-18dd18a31aad)

---

## 🚀 New in V2

- ✅ Integrated **Google Gemini 1.5 Pro** for AI-generated plan summaries
- ✅ Added `.env` support to hide API keys securely
- ✅ Enhanced UI with Streamlit components and visuals
- ✅ Deployed on **Streamlit Cloud**
- ✅ Improved model compatibility with `joblib` and fixed `.pkl` deployment bugs

---

## 📦 Tech Stack

- Streamlit
- scikit-learn
- Google Generative AI (Gemini)
- joblib
- pandas
- Python 3.12+

---

## 🔐 Setup Notes

To run locally:
1. Create `.env` and add your Gemini key:

GEMINI_API_KEY=your_key_here

markdown
Copy
Edit

2. Install dependencies:

pip install -r requirements.txt

markdown
Copy
Edit

3. Run the app:

streamlit run smart_study_app.py
