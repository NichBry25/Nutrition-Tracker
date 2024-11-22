from api import API_edamame
from nutritionlimit import nutrition
from signup import UserInputSignup
from mainpage import LoginAndSignUp, Database

if __name__ == "__main__":
    db_manager = Database()
    app = LoginAndSignUp(db_manager)
    
