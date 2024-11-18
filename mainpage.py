import sqlite3
import customtkinter as CTK
from signup import UserInputSignup
from tkinter import ttk
from nutritionlimit import nutrition
from api import API_edamame

class LoginAndSignUp:
    def __init__(self, db_manager) -> None:
        self.db_manager = db_manager
        self.gettingdata = UserInputSignup()
        # self.fooddatafromAPI = API_edamame() 
        # Later On
        CTK.set_appearance_mode("dark")
        CTK.set_default_color_theme("blue")
        self.create_entry_window()
    
    def create_entry_window(self):
        self.entry_window = CTK.CTk()
        self.entry_window.title("Nutrition Tracker")
        self.entry_window.geometry("400x400")

        CTK.CTkLabel(self.entry_window, text ="Welcome").pack(pady=10)
        
        CTK.CTkButton(self.entry_window, text="Login", command=self.create_login_page).pack(pady=10)
        CTK.CTkButton(self.entry_window, text="Sign Up", command=self.create_signup_page).pack(pady=10)

        self.entry_window.mainloop()

    def create_login_page(self):
        self.entry_window.destroy()

        self.login_window = CTK.CTk()
        self.login_window.title("Login")
        self.login_window.geometry("400x400")

        CTK.CTkLabel(self.login_window, text="Username").pack(pady=10)
        self.username_from_login = CTK.CTkEntry(self.login_window)
        self.username_from_login.pack(pady=10)
        CTK.CTkLabel(self.login_window, text="Password").pack(pady=10)
        self.password_from_login = CTK.CTkEntry(self.login_window)
        self.password_from_login.pack(pady=10)

        CTK.CTkButton(self.login_window, text = "Submit", command=self.login).pack(pady=20)

    def create_signup_page(self):
        self.entry_window.destroy()

        self.signup_window = CTK.CTk()
        self.signup_window.title("Sign Up")
        self.signup_window.geometry("400x400")

        CTK.CTkLabel(self.signup_window, text="Username").pack(pady=10)
        self.username_from_signup = CTK.CTkEntry(self.signup_window)
        self.username_from_signup.pack(pady=10)
        CTK.CTkLabel(self.signup_window, text="Password").pack(pady=5)
        self.password_from_signup = CTK.CTkEntry(self.signup_window)
        self.password_from_signup.pack(pady=5)

        CTK.CTkButton(self.signup_window, text = "Submit", command=self.signup).pack(pady=5)

    def login(self):
        username = self.username_from_login.get()
        password = self.password_from_login.get()
        user = self.db_manager.get_user(username, password)

        if user:
            user_id = user[0]
            user_info = self.db_manager.get_user_information(user_id)
            user_info_fulfilled = self.db_manager.get_user_information_fulfilled(user_id)
            self.show_main_page(user_info, user_info_fulfilled)
        else:
            CTK.CTkLabel(self.login_window, text = "Invalid username or password.").pack(pady=5)

    def signup(self):
        username = self.username_from_signup.get()
        password = self.password_from_signup.get()
        user_id = self.db_manager.add_user(username, password)

        if user_id:
            self.signup_window.destroy()
            self.gettingdata.create_first_window()

            self.db_manager.add_user_information(
                user_id, 
                self.gettingdata.user_data["sex"],
                self.gettingdata.user_data["weight"],
                self.gettingdata.user_data["height"],
                self.gettingdata.user_data["age"],
                self.gettingdata.user_data["activity"],
                self.gettingdata.user_data["fitness"],
                self.gettingdata.user_data["carbohydrates"],
                self.gettingdata.user_data["health"]
                )
        else:
            CTK.CTkLabel(self.signup_window, text = "Username already exists").pack(pady=5)

    def go_back_to_login_or_signup_page(self):
        self.signup_window.destroy()
        self.create_entry_window

    def show_main_page(self, user_info, user_info_fulfilled):
        self.login_window.destroy()

        self.main_page = CTK.CTk()
        self.main_page.title("Eat healthy!")
        self.main_page.geometry("1000x1000")

        sex, weight, height, age, activity, fitness, carbohydrates, health = user_info
        nutrition_data = self.calculate_nutrition(sex, weight, height, age, activity, fitness, carbohydrates, health)

        calories_intake, carbohydrates_intake, cholesterol_limit, fat_limit, protein_intake, sodium_limit, calcium_intake, iron_intake, potassium_intake, b12, b6a, c, d = user_info_fulfilled

        self.user_nutrition_information = ['Calories Intake: ', 'Carbohydrates Intake: ', 'Cholesterol Limit: ', 'Fat Limit: ', 'Protein Intake: ', 'Sodium Limit: ', 'Calcium Intake: ', 'Iron Intake: ', 'Potassium Intake: ', 'Vit B12 Intake: ', 'Vit B6A Intake: ', 'Vit C Intake: ', 'Vit D Intake: ']
        self.user_nutriton_fulfilled = [calories_intake, carbohydrates_intake, cholesterol_limit, fat_limit, protein_intake, sodium_limit, calcium_intake, iron_intake, potassium_intake, b12, b6a, c, d]
        self.user_nutrition_dailyneeds = [nutrition_data["caloric_intake"], 
                                          nutrition_data["carbohydrates_intake"], 
                                          nutrition_data["cholesterol_limit"], 
                                          nutrition_data["fat_limit"], 
                                          nutrition_data["protein_intake"], 
                                          nutrition_data["sodium_limit"], 
                                          nutrition_data["calcium_intake"],
                                          nutrition_data["iron_intake"],
                                          nutrition_data["potassium_intake"],
                                          nutrition_data["vitamin_b12"],
                                          nutrition_data["vitamin_b6a"],
                                          nutrition_data["vitamin_c"],
                                          nutrition_data["vitamin_d"]]
        self.user_nutrition_measurements = ['kcal', 'g', 'mg', 'g', 'g', 'mg', 'mg', 'mg', 'mg', 'microgram', 'mg', 'mg', 'microgram']

        self.table_in_mainpage = ttk.Treeview(self.main_page, columns=('Information', 'Fulfilled', 'Daily Needs', 'Measurements'), show='headings', height=14)
        self.table_in_mainpage.heading('Information', text = 'Information')
        self.table_in_mainpage.heading('Fulfilled', text = 'Fulfilled')
        self.table_in_mainpage.heading('Daily Needs', text='Daily Needs')
        self.table_in_mainpage.heading('Measurements', text='Measurements')
        self.table_in_mainpage.pack(pady=5)

        for i in range(13):
            self.table_in_mainpage.insert(parent='', index=0, values=(self.user_nutrition_information[12-i], self.user_nutriton_fulfilled[12-i], self.user_nutrition_dailyneeds[12-i], self.user_nutrition_measurements[12-i]))

        CTK.CTkButton(self.main_page, text="Exit", command=self.on_close).pack(pady=5)

    def calculate_nutrition(self, sex, weight, height, age, activity, fitness, carbohydrates, health):
        nutrition_data = nutrition(sex, weight, height, age, activity, fitness, carbohydrates, health)
        return nutrition_data
    
    def on_close(self):
        self.main_page.destroy()    

class Database:
    def __init__(self, db_name = "user_data.db") -> None:
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_information (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sex TEXT,
            weight INTEGER,
            height INTEGER,
            age INTEGER,
            activity TEXT,
            fitness TEXT,
            carbohydrates TEXT,
            health TEXT,
            FOREIGN KEY (id) REFERENCES users (id))
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_information_fulfilled (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            calories_intake INTEGER,
            carbohydrates_intake INTEGER,
            cholesterol_limit INTEGER,
            fat_limit INTEGER,
            protein_intake INTEGER,
            sodium_limit INTEGER,
            calcium_intake INTEGER,
            iron_intake INTEGER,
            potassium_intake INTEGER,
            b12 INTEGER,
            b6a INTEGER,
            c INTEGER,
            d INTEGER,
            FOREIGN KEY (id) REFERENCES users (id))
        ''')
        self.conn.commit()

    def get_user(self, username, password):
        self.cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        return self.cursor.fetchone() # Returns the ID, if it fails, it returns None

    def get_user_information(self, user_id):
        self.cursor.execute('''
            SELECT sex, weight, height, age, activity, fitness, carbohydrates, health
            FROM user_information WHERE id = ?
        ''', (user_id,))
        return self.cursor.fetchone()

    def get_user_information_fulfilled(self, user_id):
        self.cursor.execute('''
            SELECT calories_intake, carbohydrates_intake, cholesterol_limit, fat_limit, protein_intake, sodium_limit, calcium_intake, iron_intake, potassium_intake, b12, b6a, c, d
            FROM user_information_fulfilled WHERE id = ?
        ''', (user_id,))
        return self.cursor.fetchone()

    def add_user(self, username, password):
        try:
            self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            return None
    
    def add_user_information(self, user_id, sex, weight, height, age, activity, fitness, carbohydrates, health):
        self.cursor.execute('''
            INSERT INTO user_information (id, sex, weight, height, age, activity, fitness, carbohydrates, health)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, sex, weight, height, age, activity, fitness, carbohydrates, health))
        self.cursor.execute('''
            INSERT INTO user_information_fulfilled (id, calories_intake, carbohydrates_intake, cholesterol_limit, fat_limit, protein_intake, sodium_limit, calcium_intake, iron_intake, potassium_intake, b12, b6a, c, d)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

        self.conn.commit()