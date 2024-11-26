import customtkinter as CTK
from tkinter import ttk

class UserInputSignup:
    def __init__(self) -> None:
        CTK.set_appearance_mode("dark")
        CTK.set_default_color_theme("blue")
        self.user_data = {} # Storage for all data inputs in this module.
    
    def create_first_window(self):
        self.window1 = CTK.CTk()
        self.window1.title("General Information")
        self.window1.geometry("400x400")

        # User's Sex
        CTK.CTkLabel(self.window1, text="Sex:").pack(pady=5)

        radio_frame = CTK.CTkFrame(self.window1)
        radio_frame.pack(pady=5)

        self.sex_var = self.user_data.get("sex_var", CTK.StringVar())
        CTK.CTkRadioButton(radio_frame, text="Male", variable=self.sex_var, value="Male").pack(side="left", padx=10)
        CTK.CTkRadioButton(radio_frame, text="Female", variable=self.sex_var, value="Female").pack(side="left", padx=10)

        # User's Weight
        CTK.CTkLabel(self.window1, text="Weight (kg):").pack(pady=5)
        self.weight_entry = CTK.CTkEntry(self.window1)
        self.weight_entry.insert(0, self.user_data.get("weight", ""))
        self.weight_entry.pack()

        # User's Height
        CTK.CTkLabel(self.window1, text="Height (cm):").pack(pady=5)
        self.height_entry = CTK.CTkEntry(self.window1)
        self.height_entry.insert(0, self.user_data.get("height", ""))
        self.height_entry.pack()

        # User's Age
        CTK.CTkLabel(self.window1, text="Age:").pack(pady=5)
        self.age_entry = CTK.CTkEntry(self.window1)
        self.age_entry.insert(0, self.user_data.get("age", ""))
        self.age_entry.pack()

        # Button to the Next Page
        CTK.CTkButton(self.window1, 
                      text="Next", 
                      text_color="white",
                      hover_color="lightblue",
                      corner_radius= 8,
                      command=self.check_input_from_first_window).pack(pady=20)

        self.window1.mainloop()

    def check_input_from_first_window(self):
        sex = self.sex_var.get()
        weight = self.weight_entry.get()
        height = self.height_entry.get()
        age = self.age_entry.get()
        # User input checks, making sure data types are proper.
        try:
            weight = int(weight)
            height = int(height)
            age = int(age)
            if len(sex) != 0:
                # Saves the variable.
                self.user_data.update({
                    "sex": sex,
                    "weight": weight,
                    "height": height,
                    "age": age,
                    "sex_var": self.sex_var 
                })
                self.create_second_window()
            else:
                CTK.CTkLabel(self.window1, text="Must pick male or female!").pack(pady=20)
        except ValueError:
            CTK.CTkLabel(self.window1, text="Make sure to use numbers only!").pack(pady=10)
            
    def create_second_window(self):
        
        self.window1.destroy()

        self.window2 = CTK.CTk()
        self.window2.title("User Preferences")
        self.window2.geometry("600x550")

        # User's Activity Level
        CTK.CTkLabel(self.window2, text="Activity Level: ").pack(pady=5)
        self.activity_var = self.user_data.get("activity_var", CTK.StringVar())
        radio_frame2_top = CTK.CTkFrame(self.window2)
        radio_frame2_top.pack(pady=5)
        CTK.CTkRadioButton(radio_frame2_top, text="Sedentary", variable=self.activity_var, value="Sedentary").pack(side="left", padx=10)
        CTK.CTkRadioButton(radio_frame2_top, text="Lightly Active", variable=self.activity_var, value="Light").pack(side="left", padx=10)
        CTK.CTkRadioButton(radio_frame2_top, text="Moderately Active", variable=self.activity_var, value="Moderate").pack(side="left", padx=10)
        radio_frame2_bottom = CTK.CTkFrame(self.window2)
        radio_frame2_bottom.pack(pady=5)
        CTK.CTkRadioButton(radio_frame2_bottom, text="Very Active", variable=self.activity_var, value="Active").pack(side="left", padx=10)
        CTK.CTkRadioButton(radio_frame2_bottom, text="Extremely Active (Athlete)", variable=self.activity_var, value="Super Active").pack(side="left", padx=10)

        # User's Fitness Goal
        CTK.CTkLabel(self.window2, text="Fitness Goal: ").pack(pady=10)
        self.fitness_var = self.user_data.get("fitness_var", CTK.StringVar())
        radio_frame3_top = CTK.CTkFrame(self.window2)
        radio_frame3_top.pack(pady=5)
        CTK.CTkRadioButton(radio_frame3_top, text="Maintenance", variable=self.fitness_var, value="Maintenance").pack(side="left", padx=10)
        CTK.CTkRadioButton(radio_frame3_top, text="Bulking", variable=self.fitness_var, value="Bulking").pack(side="left", padx=10)
        radio_frame3_bottom = CTK.CTkFrame(self.window2)
        radio_frame3_bottom.pack(pady=5)
        CTK.CTkRadioButton(radio_frame3_bottom, text="Cutting", variable=self.fitness_var, value="Cutting").pack(side="left", padx=10)
        CTK.CTkRadioButton(radio_frame3_bottom, text="Weight-Loss", variable=self.fitness_var, value="Weight-Loss").pack(side="left", padx=10)

        # User's Carbohydrates Intake Strategy
        CTK.CTkLabel(self.window2, text="Carbohydrates Intake: ").pack(pady=10)
        self.carbs_var = self.user_data.get("carbs_var", CTK.StringVar())
        radio_frame4_top = CTK.CTkFrame(self.window2)
        radio_frame4_top.pack(pady=5)
        CTK.CTkRadioButton(radio_frame4_top, text="Maintenance", variable=self.carbs_var, value="Maintenance").pack(side="left", padx=10)
        CTK.CTkRadioButton(radio_frame4_top, text="Weight-Gain (Surplus)", variable=self.carbs_var, value="Weight-Gain").pack(side="left", padx=10)
        radio_frame4_bottom = CTK.CTkFrame(self.window2)
        radio_frame4_bottom.pack(pady=5)
        CTK.CTkRadioButton(radio_frame4_bottom, text="Weight-Loss (Deficit)", variable=self.carbs_var, value="Weight-Loss").pack(side="left", padx=10)
        CTK.CTkRadioButton(radio_frame4_bottom, text="Keto / No Carbohydrates", variable=self.carbs_var, value="Keto").pack(side="left", padx=10)

        # User's Health Conditions
        CTK.CTkLabel(self.window2, text = "Do you have any cardiac health problems?").pack(pady=10)
        self.health_var = self.user_data.get("health_var", CTK.StringVar())
        radio_frame5 = CTK.CTkFrame(self.window2)
        radio_frame5.pack(pady=5)
        CTK.CTkRadioButton(radio_frame5, text = "Yes", variable=self.health_var, value = "Yes").pack(side="left", padx=10)
        CTK.CTkRadioButton(radio_frame5, text = "No", variable=self.health_var, value = "No").pack(side="left", padx=10)

        # Button to the Next Page
        CTK.CTkButton(self.window2, 
                      text="Next", 
                      text_color="white",
                      hover_color="lightblue",
                      corner_radius= 8,
                      command=self.check_input_from_second_window).pack(pady=20)

    def check_input_from_second_window(self):
        activity = self.activity_var.get()
        fitness = self.fitness_var.get()
        carbohydrates = self.carbs_var.get()
        health = self.health_var.get()
        # Checks for null radio button inputs.
        if len(activity) != 0 and len(fitness) != 0 and len(carbohydrates) != 0 and len(health) != 0:
            self.user_data.update({
                "activity": activity,
                "fitness": fitness,
                "carbohydrates": carbohydrates,
                "health": health,
                "activity_var": self.activity_var,
                "fitness_var": self.fitness_var,
                "carbs_var": self.carbs_var,
                "health_var": self.health_var
            })
            self.confirmation_window()
        else:
            CTK.CTkLabel(self.window2, text="Make sure to fill all of the questions!").pack(pady=15)

    def confirmation_window(self):
        
        self.window2.destroy()

        self.window_confirm = CTK.CTk()
        self.window_confirm.title("Data Confirmation")
        self.window_confirm.geometry("400x400")

        self.user_preferences = ['Sex: ', 'Weight: ', 'Height: ', 'Age: ', 'Activity Level: ', 'Fitness Goal: ', 'Carbohydrate Intake: ', 'Medical Problems: ']
        # Retrieves all the data from self.user_data.
        self.user_preferences_details = [
            self.user_data.get('sex', 'N/A'),
            self.user_data.get('weight', 'N/A'),
            self.user_data.get('height', 'N/A'),
            self.user_data.get('age', 'N/A'),
            self.user_data.get('activity', 'N/A'),
            self.user_data.get('fitness', 'N/A'),
            self.user_data.get('carbohydrates', 'N/A'),
            self.user_data.get('health', 'N/A')
        ]

        CTK.CTkLabel(self.window_confirm, text="Confirm Your Details:", font=("Arial", 16)).pack(pady=5)

        # Data presented in table form.
        self.table_information = ttk.Treeview(self.window_confirm, columns=('Information', 'Details'), show='headings', height=8)
        self.table_information.heading('Information', text='Information')
        self.table_information.heading('Details', text='Details')
        self.table_information.pack(pady=0)
        for i in range(8):
            self.table_information.insert(parent='', index=0, values=(self.user_preferences[7-i], self.user_preferences_details[7-i]))

        CTK.CTkButton(self.window_confirm, 
                      text="Next", 
                      text_color="white",
                      hover_color="lightblue",
                      corner_radius= 8,
                      command=self.save_information).pack(pady=20)

        CTK.CTkButton(self.window_confirm, 
                      text="Back", 
                      text_color="white",
                      hover_color="lightblue",
                      corner_radius= 8,
                      command=self.go_back_to_front).pack(pady=20)
        
    def go_back_to_front(self):
        # Returns back to the beginning page.
        self.window_confirm.destroy()
        self.create_first_window()

    def save_information(self):
        # Data is successfully saved.
        self.window_confirm.destroy()
        self.save_window = CTK.CTk()
        self.save_window.title("Yay! Welcome.")
        self.save_window.geometry("400x50")
        CTK.CTkLabel(self.save_window, text="Your data has been saved! Close and restart the app.").pack(pady=5)
        return self.user_data

