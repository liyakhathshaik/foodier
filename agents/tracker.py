from utils.health import HealthUtils

class TrackerAnalyzerAgent:
    def collect_daily_logs(self, logs_data):
        """Collect daily logs from the request JSON payload."""
        if not logs_data:
            return None  # No logs provided

        logs = {
            "weight": logs_data.get("weight"),
            "water_intake": logs_data.get("water_intake"),
            "exercise": logs_data.get("exercise", "No").capitalize(),
            "diet_adherence": logs_data.get("diet_adherence", "No").capitalize(),
            "cheat_meal": logs_data.get("cheat_meal", "No").capitalize(),
            "cheat_meal_details": logs_data.get("cheat_meal_details", ""),  # What did they eat?
            "cheat_meal_location": logs_data.get("cheat_meal_location", ""),  # Where did they eat?
            "cheat_meal_type": logs_data.get("cheat_meal_type", ""),  # Extra or replacement?
            "skipped_meal": logs_data.get("skipped_meal", "No").capitalize(),
            "skipped_meal_type": logs_data.get("skipped_meal_type", ""),  # Which meal was skipped?
            "sleep_hours": logs_data.get("sleep_hours"),
            "steps": logs_data.get("steps"),
        }
        return logs

    def analyze_progress(self, logs, user_data):
        """Analyze daily logs and provide feedback."""
        if not logs:
            return {"message": "No logs found. Please enter today's logs or exit."}

        print("\n=== Progress Analysis ===")
        
        # Check weight progress
        current_weight = logs.get("weight")
        initial_weight = user_data.get("weight")
        if current_weight and initial_weight:
            weight_change = current_weight - initial_weight
            if weight_change < 0:
                print(f"Great job! You've lost {abs(weight_change):.2f} kg.")
            elif weight_change > 0:
                print(f"Be careful! You've gained {abs(weight_change):.2f} kg.")
            else:
                print("Your weight has remained the same.")

        # Check water intake
        water_intake = logs.get("water_intake")
        hydration_goal = user_data.get("hydration_goals", 2.5)  # Default goal: 2.5 liters
        if water_intake:
            if water_intake >= hydration_goal:
                print("You've met your daily hydration goal. Well done!")
            else:
                print(f"Drink more water! You're {hydration_goal - water_intake:.2f} liters short of your goal.")

        # Check exercise adherence
        exercise = logs.get("exercise")
        if exercise == "Yes":
            print("You followed your exercise routine today. Keep it up!")
        else:
            print("You missed your exercise routine today. Try to stay consistent!")

        # Check diet adherence
        diet_adherence = logs.get("diet_adherence")
        if diet_adherence == "Yes":
            print("You followed your diet plan today. Great work!")
        else:
            print("You strayed from your diet plan today. Stay focused!")

        # Check cheat meal
        cheat_meal = logs.get("cheat_meal")
        if cheat_meal == "Yes":
            cheat_meal_details = logs.get("cheat_meal_details")
            cheat_meal_location = logs.get("cheat_meal_location")
            cheat_meal_type = logs.get("cheat_meal_type")
            print(f"You had a cheat meal today: {cheat_meal_details} at {cheat_meal_location}.")
            if cheat_meal_type == "Extra":
                print("This was an extra meal outside your diet plan. Be mindful of your calorie intake.")
            elif cheat_meal_type == "Replacement":
                print("This meal replaced one of your regular meals. Ensure you're still meeting your nutritional goals.")

        # Check skipped meal
        skipped_meal = logs.get("skipped_meal")
        skipped_meal_type = logs.get("skipped_meal_type")
        if skipped_meal == "Yes":
            print(f"You skipped {skipped_meal_type} today. Try to stick to your meal plan to avoid nutrient deficiencies.")

        # Check sleep hours
        sleep_hours = logs.get("sleep_hours")
        if sleep_hours:
            if sleep_hours >= 7:
                print("You met your sleep goal. Great job!")
            else:
                print(f"Try to sleep more. You only got {sleep_hours} hours last night.")

        # Check steps
        steps = logs.get("steps")
        step_goal = user_data.get("step_goal", 10000)  # Default goal: 10,000 steps
        if steps:
            if steps >= step_goal:
                print("You met your daily step goal. Great job!")
            else:
                print(f"You're {step_goal - steps} steps short of your goal. Keep moving!")

        # Calculate BMI and provide health insights
        bmi, bmi_category = HealthUtils.calculate_bmi(user_data.get("weight"), user_data.get("height"))
        print(f"\nYour BMI is {bmi:.1f}, which is categorized as {bmi_category}.")

        return {"message": "Progress analyzed successfully!", "bmi": bmi, "bmi_category": bmi_category}

    def generate_weekly_report(self, user_data):
        logs = user_data.get("logs", [])
        if not logs:
            return "No logs found for this week."

        total_weight_change = 0
        total_water_intake = 0
        exercise_days = 0
        diet_days = 0
        cheat_meals = 0
        skipped_meals = 0
        total_sleep_hours = 0
        total_steps = 0

        for log in logs:
            total_weight_change += log.get("weight", 0) - user_data.get("weight", 0)
            total_water_intake += log.get("water_intake", 0)
            if log.get("exercise") == "Yes":
                exercise_days += 1
            if log.get("diet_adherence") == "Yes":
                diet_days += 1
            if log.get("cheat_meal") == "Yes":
                cheat_meals += 1
            if log.get("skipped_meal") == "Yes":
                skipped_meals += 1
            total_sleep_hours += log.get("sleep_hours", 0)
            total_steps += log.get("steps", 0)

        report = (
            f"Weekly Weight Change: {total_weight_change:.2f} kg\n"
            f"Average Daily Water Intake: {total_water_intake / len(logs):.2f} liters\n"
            f"Days Exercised: {exercise_days}/{len(logs)}\n"
            f"Days Followed Diet: {diet_days}/{len(logs)}\n"
            f"Cheat Meals: {cheat_meals}\n"
            f"Skipped Meals: {skipped_meals}\n"
            f"Average Sleep Hours: {total_sleep_hours / len(logs):.1f}\n"
            f"Average Daily Steps: {total_steps / len(logs):.0f}"
        )
        return report