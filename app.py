import streamlit as st
from together import Together

# Set up the Streamlit app
st.set_page_config(page_title="BodyFuel AI", layout="centered")

# Display logo at the top (centered and resized)
st.image("body-fuel-logo.png", width=1000, caption="BodyFuel AI Logo")

# Title and description
st.title("BodyFuel AI - Macro Calculator & Meal Planner")
st.write("An AI-powered app to help you calculate your macros, generate meal plans, and create grocery lists tailored to your fitness goals.")

# User Inputs
st.header("Enter Your Details")
weight_lb = st.number_input("Weight (lbs)", min_value=66, max_value=440, value=154)
height_ft = st.number_input("Height (feet)", min_value=3, max_value=8, value=5)
height_in = st.number_input("Height (inches)", min_value=0, max_value=11, value=7)
age = st.number_input("Age", min_value=10, max_value=100, value=25)
gender = st.selectbox("Gender", ["Male", "Female"])
worked_out_today = st.selectbox(
    "Did you work out today?",
    ["No", "Light workout", "Moderate workout", "Intense workout"]
)
goal = st.selectbox(
    "Goal",
    ["Lose Fat", "Maintain Weight", "Build Muscle"]
)
dietary_preference = st.selectbox("Dietary Preference", ["Regular", "Vegan", "Vegetarian", "Keto", "Paleo"])
meal_type = st.selectbox("Select Meal Type", ["Breakfast", "Lunch", "Dinner", "All"])

# Convert weight to kg and height to cm
weight = weight_lb * 0.453592  # 1 lb = 0.453592 kg
height = (height_ft * 12 + height_in) * 2.54  # Convert feet and inches to cm

# Calculate Basal Metabolic Rate (BMR)
if gender == "Male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

# Adjust BMR based on workout intensity
workout_multiplier = {
    "No": 1.2,
    "Light workout": 1.375,
    "Moderate workout": 1.55,
    "Intense workout": 1.725
}
tdee = bmr * workout_multiplier[worked_out_today]

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
    # Initialize Together.ai client with API key
    client = Together(api_key=st.secrets["together_api_key"])

    # API request parameters
    model = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
    prompt = (
        f"You are a professional nutrition assistant. Generate exactly 3 {meal_type.lower()} recipe options for a person whose goal is {goal.lower()}, "
        f"with a daily caloric intake of {calories:.0f} kcal. The meal plan should be suitable for a {dietary_preference.lower()} diet. "
        "Each recipe should include a short description, the list of ingredients, and step-by-step preparation instructions. Please keep the responses concise."
    )

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": prompt}],
            max_tokens=700,
            temperature=0.7,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stream=True
        )

        # Stream response and accumulate the result
        result = ""
        for token in response:
            if hasattr(token, "choices"):
                result += token.choices[0].delta.content

        # Display the final accumulated result
        st.subheader(f"Generated {meal_type} Meal Plan")
        st.write(result)

    except Exception as e:
        st.error(f"Unexpected error: {e}")
