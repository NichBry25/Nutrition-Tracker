# This function takes in 8 arguments given by the signup.py module and is going to return the user's needed daily nutrition!

def nutrition(sex, weight_kg, height_cm, age, activity_level, fitness_goal, carb_intake, health_condition):
    # Caloric intake.
    if sex == "Male":
        BMR = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif sex == "Female":
        BMR = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:
        raise ValueError("Invalid sex. Please enter 'male' or 'female'.")
    activity_adjustment = {
        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Active": 1.725,
        "Super Active": 1.9
    }
    BMR *= activity_adjustment[activity_level]

    # Carbs intake.
    carbs_limit = {
        "Maintenance": 0.5,
        "Weight-Gain": 0.55,
        "Weight-Loss": 0.375,
        "Keto": 0.075
    }
    carbohydrates = BMR * carbs_limit[carb_intake]

    # Cholesterol limit.
    if health_condition == "Yes":
        cholesterol = 200
    else:
        cholesterol = 300

    # Fat intake.
    fat_limit = {
        "Maintenance": 0.275,
        "Bulking": 0.25,
        "Cutting": 0.2,
        "Weight-Loss": 0.225
    }
    fat = BMR * fat_limit[fitness_goal]

    # Protein intake.
    protein_goal = {
        "Maintenance": 1.4,
        "Bulking": 1.9,
        "Cutting": 2.25,
        "Weight-Loss": 2.1
    }
    protein = weight_kg * protein_goal[fitness_goal]

    # Sodium limit.
    sodium = 2000

    # Calcium intake.
    if age <= 1:
        calcium = 240
    elif 1 < age <= 3:
        calcium = 700
    elif 4 <= age <= 8:
        calcium = 1000
    elif 9 <= age <= 18:
        calcium = 1300
    elif 19 <= age <= 50:
        calcium = 1000
    elif 51 <= age <= 70:
        if sex == "Female":
            calcium = 1200
        elif sex == "Male":
            calcium = 1000
    elif age > 70:
        calcium = 1200

    # Iron intake.
    if age <= 1:
        iron = 11
    elif 1 < age <= 3:
        iron = 7   
    elif 4 <= age <= 8:
        iron = 10
    elif 9 <= age <= 13:
        iron = 13
    elif 14 <= age <= 18:
        if sex == "Male":
            iron = 11
        elif sex == "Female":
            iron = 15
    elif 19 <= age <= 50:
        if sex == "Male":
            iron = 8
        elif sex == "Female":
            iron = 18
    elif age > 50:
        iron = 8

    # Potassium intake.
    if age <= 1:
        potassium = 550
    elif 1 < age <= 3:
        potassium = 3000
    elif 4 <= age <= 8:
        potassium = 3800
    elif 9 <= age <= 13:
        potassium = 4500
    elif age >= 14:
        potassium = 4700

    # Vitamin B-12 intake.
    if age <= 1:
        vitb12 = 0.45
    elif 1 < age <= 3:
        vitb12 = 0.9
    elif 4 <= age <= 8:
        vitb12 = 1.2
    elif 9 <= age <= 13:
        vitb12 = 1.8
    elif age >= 14:
        vitb12 = 2.4

    # Vitamin B-6A intake.
    if age <= 1:
        vitb6a = 0.2
    elif 1 < age <= 3:
        vitb6a = 0.5
    elif 4 <= age <= 8:
        vitb6a = 0.6
    elif 9 <= age <= 13:
        vitb6a = 1
    elif 14 <= age <= 18:
        vitb6a = 1.3
    elif 19 <= age <= 50:
        vitb6a = 1.3
    elif age >= 51:
        if sex == "Female":
            vitb6a = 1.5
        elif sex == "Male":
            vitb6a = 1.7

    # Vitamin C intake.
    if age <= 1:
        vitc = 45
    elif 1 < age <= 3:
        vitc = 15
    elif 4 <= age <= 8:
        vitc = 25
    elif 9 <= age <= 13:
        vitc = 45
    elif 14 <= age <= 18:
        if sex == "Male":
            vitc = 75
        elif sex == "Female":
            vitc = 65
    elif age >= 19:
        if sex == "Male":
            vitc = 90
        elif sex == "Female":
            vitc = 75

    # Vitamin D intake.
    if age <= 1:
        vitd = 10
    elif 1 < age <= 70:
        vitd = 15
    elif age >= 71:
        vitd = 20

    return {
        "caloric_intake": BMR,
        "carbohydrates_intake": carbohydrates,
        "cholesterol_limit": cholesterol,
        "fat_limit": fat,
        "protein_intake": protein,
        "sodium_limit": sodium,
        "calcium_intake": calcium,
        "iron_intake": iron,
        "potassium_intake": potassium,
        "vitamin_b12": vitb12,
        "vitamin_b6a": vitb6a,
        "vitamin_c": vitc,
        "vitamin_d": vitd
    }




 
