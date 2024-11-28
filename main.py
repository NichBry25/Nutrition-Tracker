from mainpage import Application, Database

# Initializing the running program.
if __name__ == "__main__":
    db_manager = Database()
    app = Application(db_manager)
    
