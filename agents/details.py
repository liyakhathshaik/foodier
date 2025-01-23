class DietFitnessAgent:
    def collect_user_inputs(self):
        print("=== Create Your Profile ===")
        user_data = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "gender": input("Enter your gender (Male/Female/Other): ").capitalize(),
            "weight": float(input("Enter your weight (kg): ")),
            "height": float(input("Enter your height (cm): ")),
            "activity_level": input("What is your activity level? (Sedentary/Lightly Active/Moderately Active/Very Active): ").capitalize(),
            "medical_conditions": input("Do you have any medical conditions? (e.g., diabetes, hypertension, PCOS, pregnancy): "),
            "allergies": input("Do you have any allergies? (e.g., nuts, gluten, dairy): "),
            "meals_per_day": int(input("How many meals do you eat per day? (e.g., 3 meals, 5 small meals): ")),
            "cooking_preferences": input("What are your cooking preferences? (Home-cooked/Ready-to-eat/Mix): ").capitalize(),
            "stress_levels": input("What are your stress levels? (Low/Medium/High): ").capitalize(),
            "emotional_eating": input("Do you have any emotional eating habits? (e.g., stress eating, binge eating): "),
            "state": input("Which Indian state are you from? (e.g., Tamil Nadu, Punjab, Gujarat): ").capitalize(),
            "diet_duration": input("How long do you need the diet plan for? (e.g., 1 week, 2 weeks, 1 month, custom days): ").lower(),
            "dietary_preference": input("What is your dietary preference? (Vegetarian/Non-Vegetarian/Vegan/Keto/Gluten-free): ").capitalize(),
            "dietary_exceptions": input("Are there any specific foods you avoid? (e.g., no beef, no pork): "),
            "goal": input("What is your goal? (Gym Bulking/Gym Cutting/Pregnancy/Healthy/Weight Gain/Weight Loss/Sports): ").capitalize(),
        }

        # Additional health-related inputs
        user_data["bp"] = input("Enter your blood pressure (e.g., 120/80): ")
        has_sugar = input("Do you have diabetes or high sugar levels? (Yes/No): ").capitalize()
        if has_sugar == "Yes":
            user_data["sugar_level"] = float(input("Enter your fasting sugar level (mg/dL): "))
        else:
            user_data["sugar_level"] = None

        # Fitness and lifestyle inputs
        user_data["fitness_goal"] = input("What is your primary fitness goal? (Weight Loss/Muscle Gain/Maintenance/Endurance): ").capitalize()
        user_data["exercise_frequency"] = input("How often do you exercise? (e.g., 3 times a week, daily): ")
        user_data["water_intake"] = float(input("How much water do you drink daily (in liters)? "))

        # Body metrics
        print("\n=== Body Measurements ===")
        user_data["chest"] = float(input("Enter your chest measurement (in cm): "))
        user_data["waist"] = float(input("Enter your waist measurement (in cm): "))
        user_data["hip"] = float(input("Enter your hip measurement (in cm): "))
        user_data["thighs"] = float(input("Enter your thighs measurement (in cm): "))
        user_data["arms"] = float(input("Enter your arms measurement (in cm): "))

        # Advanced metrics (optional)
        user_data["body_fat_percentage"] = input("Do you know your body fat percentage? (If yes, enter the value; otherwise, leave blank): ") or None

        # Psychological and emotional factors
        user_data["motivation_levels"] = input("How motivated are you to follow a diet and fitness plan? (Low/Medium/High): ").capitalize()
        user_data["support_system"] = input("Do you have a support system (e.g., family, friends, trainer)? (Yes/No): ").capitalize()

        # Optional enhancements
        user_data["sleep_duration"] = float(input("How many hours do you sleep per night? "))
        user_data["supplements"] = input("Do you take any supplements? (e.g., protein powder, multivitamins): ")
        user_data["cuisine_preference"] = input("What are your favorite cuisines? (e.g., South Indian, North Indian, Continental): ")
        user_data["food_tracking"] = input("Do you track your food intake? (Yes/No): ").capitalize()

        return user_data