import google.generativeai as genai

class GeminiAPIAgent:
    def __init__(self):
        """Initialize the Gemini API."""
        self.model = genai.GenerativeModel('gemini-pro')  # Use the free-tier model

    def generate_diet_plan(self, user_data):
        """Generate a personalized diet plan and a general outline of the person based on user data."""
        # Generate the diet plan
        diet_plan_prompt = f"""
        Create a personalized diet plan for the following user:
        - Name: {user_data.get("name", "User")}
        - Age: {user_data.get("age", "N/A")}
        - Gender: {user_data.get("gender", "N/A")}
        - Weight: {user_data.get("weight", "N/A")} kg
        - Height: {user_data.get("height", "N/A")} cm
        - Activity Level: {user_data.get("activity_level", "N/A")}
        - Medical Conditions: {user_data.get("medical_conditions", "None")}
        - Allergies: {user_data.get("allergies", "None")}
        - Meal Preferences: {user_data.get("meals_per_day", "N/A")} meals per day, {user_data.get("cooking_preferences", "N/A")} cooking.
        - Stress Levels: {user_data.get("stress_levels", "N/A")}
        - Emotional Eating Habits: {user_data.get("emotional_eating", "N/A")}
        - State: {user_data.get("state", "N/A")}
        - Diet Duration: {user_data.get("diet_duration", "1 week")}
        - Dietary Preference: {user_data.get("dietary_preference", "N/A")}
        - Dietary Exceptions: {user_data.get("dietary_exceptions", "None")}
        - Goal: {user_data.get("goal", "N/A")}
        - Fitness Goal: {user_data.get("fitness_goal", "N/A")}
        - Exercise Frequency: {user_data.get("exercise_frequency", "N/A")}
        - Water Intake: {user_data.get("water_intake", "N/A")} liters per day
        - Body Fat Percentage: {user_data.get("body_fat_percentage", "N/A")}
        - Waist Circumference: {user_data.get("waist_circumference", "N/A")} cm
        - Chest: {user_data.get("chest", "N/A")} cm
        - Waist: {user_data.get("waist", "N/A")} cm
        - Hip: {user_data.get("hip", "N/A")} cm
        - Thighs: {user_data.get("thighs", "N/A")} cm
        - Arms: {user_data.get("arms", "N/A")} cm
        - Sleep Duration: {user_data.get("sleep_duration", "N/A")} hours per night
        - Supplements: {user_data.get("supplements", "None")}
        - Cuisine Preference: {user_data.get("cuisine_preference", "N/A")}
        - Food Tracking: {user_data.get("food_tracking", "N/A")}
        - Motivation Levels: {user_data.get("motivation_levels", "N/A")}
        - Support System: {user_data.get("support_system", "N/A")}

        Provide a {user_data.get("diet_duration", "1 week")} diet plan with:
        - Breakfast, lunch, dinner, and snacks.
        - Portion sizes and nutritional breakdown (calories, proteins, carbs, fats, vitamins, etc.).
        - Focus on regional cuisine from {user_data.get("state", "India")}.
        - Respect dietary preferences: {user_data.get("dietary_preference", "N/A")} and exceptions: {user_data.get("dietary_exceptions", "None")}.
        - Align with the user's goal: {user_data.get("goal", "N/A")} and fitness goal: {user_data.get("fitness_goal", "N/A")}.

        Format the diet plan in a table with the following columns:
        - Day
        - Meal Type (Breakfast, Lunch, Dinner, Snacks)
        - Meal Item
        - Portion Size
        - Calories
        - Proteins (g)
        - Carbs (g)
        - Fats (g)
        - Vitamins
        - Other Nutrients

        Do not include cooking instructions. Be precise and detailed about the nutritional values.
        """
        diet_plan_response = self.model.generate_content(diet_plan_prompt)
        diet_plan = diet_plan_response.text

        # Generate a general outline of the person
        outline_prompt = f"""
        Based on the following user data, create a general outline of the person's condition, lifestyle, and goals:
        - Name: {user_data.get("name", "User")}
        - Age: {user_data.get("age", "N/A")}
        - Gender: {user_data.get("gender", "N/A")}
        - Weight: {user_data.get("weight", "N/A")} kg
        - Height: {user_data.get("height", "N/A")} cm
        - Activity Level: {user_data.get("activity_level", "N/A")}
        - Medical Conditions: {user_data.get("medical_conditions", "None")}
        - Allergies: {user_data.get("allergies", "None")}
        - Meal Preferences: {user_data.get("meals_per_day", "N/A")} meals per day, {user_data.get("cooking_preferences", "N/A")} cooking.
        - Stress Levels: {user_data.get("stress_levels", "N/A")}
        - Emotional Eating Habits: {user_data.get("emotional_eating", "N/A")}
        - State: {user_data.get("state", "N/A")}
        - Diet Duration: {user_data.get("diet_duration", "1 week")}
        - Dietary Preference: {user_data.get("dietary_preference", "N/A")}
        - Dietary Exceptions: {user_data.get("dietary_exceptions", "None")}
        - Goal: {user_data.get("goal", "N/A")}
        - Fitness Goal: {user_data.get("fitness_goal", "N/A")}
        - Exercise Frequency: {user_data.get("exercise_frequency", "N/A")}
        - Water Intake: {user_data.get("water_intake", "N/A")} liters per day
        - Body Fat Percentage: {user_data.get("body_fat_percentage", "N/A")}
        - Waist Circumference: {user_data.get("waist_circumference", "N/A")} cm
        - Chest: {user_data.get("chest", "N/A")} cm
        - Waist: {user_data.get("waist", "N/A")} cm
        - Hip: {user_data.get("hip", "N/A")} cm
        - Thighs: {user_data.get("thighs", "N/A")} cm
        - Arms: {user_data.get("arms", "N/A")} cm
        - Sleep Duration: {user_data.get("sleep_duration", "N/A")} hours per night
        - Supplements: {user_data.get("supplements", "None")}
        - Cuisine Preference: {user_data.get("cuisine_preference", "N/A")}
        - Food Tracking: {user_data.get("food_tracking", "N/A")}
        - Motivation Levels: {user_data.get("motivation_levels", "N/A")}
        - Support System: {user_data.get("support_system", "N/A")}

        The outline should include:
        1. A description of the person's current physical condition (e.g., overweight, athletic, underweight).
        2. Their fitness and health goals (e.g., weight loss, muscle gain, improved endurance).
        3. Any challenges they might face (e.g., emotional eating, lack of motivation, medical conditions).
        4. Their lifestyle habits (e.g., sedentary, active, irregular sleep).
        5. A summary of their dietary preferences and restrictions.
        6. Their motivation levels and support system.

        Be concise but detailed. Use bullet points for clarity.
        """
        outline_response = self.model.generate_content(outline_prompt)
        outline = outline_response.text

        return diet_plan, outline