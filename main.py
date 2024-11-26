from mainpage import LoginAndSignUp, Database

# Initializing the running program.
if __name__ == "__main__":
    db_manager = Database()
    app = LoginAndSignUp(db_manager)
    
