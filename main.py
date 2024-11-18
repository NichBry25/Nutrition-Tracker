from api import API_edamame
from nutritionlimit import nutrition
from signup import UserInputSignup
from mainpage import LoginAndSignUp, Database

if __name__ == "__main__":
    # food_data = API_edamame()
    # food_data.nutritional_data("100 grams of salmon, 100 grams of rice")
    # API is working fine.

    db_manager = Database()
    app = LoginAndSignUp(db_manager)
    # App call is good.
    
