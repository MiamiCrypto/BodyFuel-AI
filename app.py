import streamlit as st
import requests

# Set page title and layout
st.set_page_config(page_title="BodyFuel AI", layout="centered")

# Title and description
st.title("BodyFuel AI - Macro Calculator & Meal Planner")
st.write("An AI-powered app to help you calculate your macros, generate meal plans, and create grocery lists.")

# User Inputs
st.header("Enter Your Details")
weight_lb = st.number_input("Weight (lbs)", min_value=66, max_value=440, value=154)
height_in = st.number_input("Height (inches)", min_value=40, max_value=100, value=68)
age = st.number_input("Age", min_value=10, max_value=100, value=25)
gender = st.selectbox("Gender", ["Male", "Female"])
activity_level = st.selectbox(
    "Activity Level",
    ["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"]
)
goal = st.selectbox(
    "Goal",
    ["Lose Fat", "Maintain Weight", "Build Muscle"]
)

# Convert weight to kg and height to cm
weight = weight_lb * 0.453592  # 1 lb = 0.453592 kg
height = height_in * 2.54      # 1 inch = 2.54 cm

# Calculate Basal Metabolic Rate (BMR)
if gender == "Male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

# Adjust BMR based on activity level
activity_multiplier = {
    "Sedentary": 1.2,
    "Lightly active": 1.375,
    "Moderately active": 1.55,
    "Very active": 1.725,
    "Extra active": 1.9
}
tdee = bmr * activity_multiplier[activity_level]

# Adjust calories based on goal
if goal == "Lose Fat":
    calories = tdee - 500
elif goal == "Build Muscle":
    calories = tdee + 500
else:
    calories = tdee

st.subheader(f"Your daily calorie needs: {calories:.0f} kcal")

# Macro breakdown
protein = 2.0 * weight  # 2g per kg of weight
fat = 0.8 * weight  # 0.8g per kg of weight
carbs = (calories - (protein * 4 + fat * 9)) / 4

st.subheader("Your Daily Macronutrient Targets")
st.write(f"Protein: {protein:.0f}g")
st.write(f"Fat: {fat:.0f}g")
st.write(f"Carbs: {carbs:.0f}g")

# AI Meal Plan Generation
st.header("AI-Generated Meal Plan")

if st.button("Generate Meal Plan"):
    # Together.ai API configuration
    API_URL = "https://api.together.ai/generate"
    API_KEY = st.secrets["together_ai_key"]  # Add your Together.ai API key in Streamlit Cloud

    prompt = f"Generate a meal plan with {calories:.0f} kcal for {goal.lower()} and include ingredients and instructions."
    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        "prompt": prompt,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "max_tokens": 512,
        "repetition_penalty": 1
    }

    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()["choices"][0]["text"]
        st.subheader("Generated Meal Plan")
        st.write(result)
    else:
        st.error("Failed to generate the meal plan. Please try again.")
