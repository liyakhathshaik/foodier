class HealthUtils:
    @staticmethod
    def calculate_bmi(weight, height):
        """Calculate BMI and provide health insights."""
        height_in_meters = height / 100  # Convert height from cm to meters
        bmi = weight / (height_in_meters ** 2)
        if bmi < 18.5:
            return bmi, "Underweight"
        elif 18.5 <= bmi < 25:
            return bmi, "Normal weight"
        elif 25 <= bmi < 30:
            return bmi, "Overweight"
        else:
            return bmi, "Obese"