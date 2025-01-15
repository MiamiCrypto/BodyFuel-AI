import streamlit as st
import requests

# Streamlit UI setup
st.title("BodyFuel AI - AI-Powered Meal Planner")
st.write("Get a personalized meal plan tailored to your fitness goals using AI.")

# User inputs
goal = st.selectbox("Select Your Goal", ["Fat Loss", "Muscle Gain", "Maintenance"])
calories = st.number_input("Enter Your Daily Caloric Intake", min_value=1000, max_value=4000, value=2000)
dietary_preference = st.selectbox("Select Dietary Preference", ["Regular", "Vegan", "Vegetarian", "Keto", "Paleo"])

if st.button("Generate Meal Plan"):
    # Together.ai API configuration
    API_URL = "https://api.together.ai/generate"
    API_KEY = st.secrets["together_ai_key"]  # Add your Together.ai API key in Streamlit Cloud

    # API payload
    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        "prompt": f"Generate a detailed meal plan for {goal.lower()} with {calories:.0f} kcal per day. "
                  f"The meal plan should be suitable for a {dietary_preference.lower()} diet and include "
                  "breakfast, lunch, dinner, and snacks. Provide the ingredients and step-by-step instructions for each meal.",
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 40,
        "max_tokens": 512,
        "repetition_penalty": 1.1
    }

    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()["choices"][0]["text"]
        st.subheader("Generated Meal Plan")
        st.write(result)
    else:
        st.error("Failed to generate the meal plan. Please try again.")
