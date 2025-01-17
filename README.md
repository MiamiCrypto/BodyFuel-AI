BodyFuel AI

BodyFuel AI is an AI-powered web application designed to help users calculate their daily macro needs, generate personalized meal plans, and create tailored grocery lists to achieve their fitness goals. Whether your goal is to lose fat, maintain weight, or build muscle, BodyFuel AI provides actionable insights and meal recommendations to keep you on track.

Features

1. Macro Calculator

Calculates daily calorie requirements based on user-provided details (weight, height, age, gender, and activity level).

Adjusts caloric needs for fitness goals: Lose Fat, Maintain Weight, or Build Muscle.

Breaks down macronutrient targets for protein, fat, and carbohydrates.

2. AI-Generated Meal Plans

Generates meal plans tailored to user preferences:

Breakfast, Lunch, Dinner, or All meals for the day.

Dietary preferences: Regular, Vegan, Vegetarian, Keto, or Paleo.

Provides detailed recipes, including:

A short description.

Ingredients list.

Step-by-step preparation instructions.

Designed for beginners with clear cooking tips and approximate preparation times.

3. Dynamic Recipe Diversity

Recipes vary with each generation, offering unique meal options every time.

Supports creative ingredient combinations and global cuisines.

4. Responsive Web App

Streamlit-based interface for ease of use.

Mobile and desktop-friendly layout.

How to Use

1. Set Up Your Environment

Prerequisites

Python 3.8 or higher

Streamlit

Together AI API key

Installation

Clone the repository and navigate to the project directory:

git clone https://github.com/your-username/bodyfuel-ai.git
cd bodyfuel-ai

Install the required Python libraries:

pip install -r requirements.txt

2. Configure API Key

Create a .streamlit/secrets.toml file in the project directory and add your Together AI API key:

[together_api_key]
key = "your_api_key_here"

3. Run the Application

Start the Streamlit app:

streamlit run app.py

4. Access the App

Open your browser and navigate to:

http://localhost:8501

File Structure

bodyfuel-ai/
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── .streamlit/           # Streamlit configuration directory
│   └── secrets.toml      # API key for Together AI
├── body-fuel-logo.png    # Application logo
└── README.md             # Documentation

Key Features in Code

AI Integration

Uses the Together AI meta-llama/Llama-3.3-70B-Instruct-Turbo-Free model for:

Generating meal plans with detailed and diverse recipes.

Providing clear, beginner-friendly instructions.

Open Graph Metadata

Includes Open Graph meta tags for link sharing, ensuring the app displays a custom logo and description when shared on social media or messaging platforms.

Future Improvements

Add user authentication for saving preferences and meal plans.

Integrate grocery delivery APIs for one-click shopping.

Expand recipe database for more regional and seasonal variety.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For feedback or inquiries, please contact:

Email: miamicryptolabs@gmail.com

GitHub: Miami Crypto

Enjoy planning your meals with BodyFuel AI!
