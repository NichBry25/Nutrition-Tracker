from api import API_edamame
from nutritionlimit import nutrition
from signup import UserInputSignup

if __name__ == "__main__":
    food_data = API_edamame()
    food_data.nutritional_data("100 grams of salmon, 100 grams of rice")

    App = UserInputSignup()

    nbhealth = nutrition(App.user_data["sex"],
                         App.user_data["weight"],
                         App.user_data["height"],
                         App.user_data["age"],
                         App.user_data["activity"],
                         App.user_data["fitness"],
                         App.user_data["carbohydrates"],
                         App.user_data["health"],)
    
    print(nbhealth)
