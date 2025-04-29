import os
import streamlit as st
import pandas as pd
import joblib
import datetime
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro")

def generate_full_study_plan(hours, difficulty, days, style):
    prompt = f"""
You are an expert AI study planner.
Generate a personalized 1-day study plan for a student with:

- Study time: {hours} hours/day
- Subject difficulty: {difficulty}
- Exam in: {days} days
- Learning style: {style}

Structure your answer clearly:
1. 🎯 Focus Time
2. 📖 Review Time
3. 🧠 Strategy
4. ⚡ Tips
5. 💬 Motivation

Use warm, motivating language. No unnecessary repetition. Max 6 bullet points.
"""
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Smart Study Planner 🧠", page_icon="📘", layout="centered")

st.title("📘 Smart Study Planner")
st.markdown("#### Get your personalized **AI-powered study plan** in seconds!")

hours = st.slider("🕒 How many hours can you study daily?", 1, 6, 3)
difficulty = st.selectbox("📚 How difficult is your subject?", ['Easy', 'Medium', 'Hard'])
days = st.slider("📅 How many days are left until the exam?", 3, 30, 10)
style = st.selectbox("🎧 What is your learning style?", ['Visual', 'Auditory', 'Kinesthetic'])

difficulty_map = {'Easy': 0, 'Medium': 1, 'Hard': 2}
learning_map = {'Visual': 0, 'Auditory': 1, 'Kinesthetic': 2}
input_data = pd.DataFrame([[
    hours,
    difficulty_map[difficulty],
    days,
    learning_map[style]
]], columns=["Daily_Hours", "Difficulty", "Days_To_Exam", "Learning_Style"])

model_ml = joblib.load('study_plan_model.pkl')

tips = {
    'Visual': "🖼️ Use diagrams, mind maps, and color coding.",
    'Auditory': "🎧 Read notes aloud or use voice recordings.",
    'Kinesthetic': "🤸 Use flashcards, drawing, or movement-based tasks."
}
techniques = {
    'Easy': "📗 Light review and summarizing should work fine.",
    'Medium': "⏱️ Try spaced repetition + summary notes.",
    'Hard': "🔥 Use Pomodoro + active recall daily."
}

if st.button("🎯 Generate Study Breakdown"):
    prediction = model_ml.predict(input_data)[0]
    focus_hours = round(hours * prediction, 1)
    review_hours = round(hours - focus_hours, 1)

    urgency = "🚨 **Your exam is very close! Focus mode ON!**" if days <= 5 else ""

    st.success("✅ Your Smart Study Plan:")
    st.markdown(f"📌 **Focus on hardest subject**: `{focus_hours} hours/day`")
    st.markdown(f"📖 **Review other subjects**: `{review_hours} hours/day`")
    st.markdown(f"💡 **Recommended learning style**: `{style}`")

    if urgency:
        st.error(urgency)

    st.info(tips[style])
    st.markdown(f"🧠 Strategy tip for {difficulty.lower()} subject: {techniques[difficulty]}")

    base_plan = f"""
SmartStudy Plan - {datetime.date.today()}

Daily Study Hours: {hours}
Subject Difficulty: {difficulty}
Days Until Exam: {days}
Learning Style: {style}

Focus Hours: {focus_hours}
Review Hours: {review_hours}

Style Tip: {tips[style]}
Technique Tip: {techniques[difficulty]}
"""
    st.download_button("💾 Save My Plan as TXT", data=base_plan, file_name="Study_Plan_Breakdown.txt", mime="text/plain")

if st.button("🧠 Generate Full AI Study Plan (Gemini)"):
    ai_output = generate_full_study_plan(hours, difficulty, days, style)
    st.markdown("---")
    st.markdown("### 💬 Your Personalized AI Study Plan:")
    st.markdown(ai_output)
    st.download_button("💾 Save Full AI Plan", data=ai_output, file_name="Full_AI_Study_Plan.txt", mime="text/plain")
