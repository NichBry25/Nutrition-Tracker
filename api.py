import requests
import json

class API_edamame:
    API_URL = "https://api.edamam.com/api/nutrition-data"
    APP_ID = "03646183"
    API_KEY = "721dd245ca8f09664b5a301bcbd4a953"

    def parameters(self, food):
        params = {
        "app_id": API_edamame.APP_ID,
        "app_key": API_edamame.API_KEY,
        "ingr": food
        }
        response = requests.get(API_edamame.API_URL, params=params)
        return response
    
    def nutritional_data(self, food):
        response = self.parameters(food)
        if response.status_code == 200:
            data = response.json()
            # Gets calories data.
            calories_amount = data.get("totalNutrients", {}).get("ENERC_KCAL", {"quantity": "0", "unit": "kcal"})
            print(f"Calorie: {calories_amount["quantity"]} {calories_amount["unit"]}")
            # Gets carbohydates data.
            carbs_amount = data.get("totalNutrients", {}).get("CHOCDF.net", {"quantity": "0", "unit": "g"})
            print(f"Carbohydrate: {carbs_amount["quantity"]} {carbs_amount["unit"]}")
            # Gets cholesteorol data.
            chole_amount = data.get("totalNutrients", {}).get("CHOLE", {"quantity": "0", "unit": "mg"})
            print(f"Cholesterol: {chole_amount["quantity"]} {chole_amount["unit"]}")
            # Gets fats data.
            fat_amount = data.get("totalNutrients", {}).get("FAT", {"quantity": "0", "unit": "g"})
            print(f"Fat: {fat_amount["quantity"]} {fat_amount["unit"]}")
            # Gets protein data.
            protein_amount = data.get("totalNutrients", {}).get("PROCNT", {"quantity": "0", "unit": "g"})
            print(f"Protein: {protein_amount["quantity"]} {protein_amount["unit"]}")
            # Gets sodium data.
            sodium_amount = data.get("totalNutrients", {}).get("NA", {"quantity": "0", "unit": "mg"})
            print(f"Sodium: {sodium_amount["quantity"]} {sodium_amount["unit"]}")
            # Gets calcium data.
            calcium_amount = data.get("totalNutrients", {}).get("CA", {"quantity": "0", "unit": "mg"})
            print(f"Calcium: {calcium_amount["quantity"]} {calcium_amount["unit"]}")
            # Gets iron data.
            iron_amount = data.get("totalNutrients", {}).get("FE", {"quantity": "0", "unit": "mg"})
            print(f"Iron: {iron_amount["quantity"]} {iron_amount["unit"]}")
            # Gets potassium data.
            potas_amount = data.get("totalNutrients", {}).get("K", {"quantity": "0", "unit": "mg"})
            print(f"Potassium: {potas_amount["quantity"]} {potas_amount["unit"]}")
            # Gets vitamin B12 data.
            vitB12_amount = data.get("totalNutrients", {}).get("VITB12", {"quantity": "0", "unit": "N/A"})
            print(f"Vitamin B-12: {vitB12_amount["quantity"]} {vitB12_amount["unit"]}")
            # Gets vitamin B6A data.
            vitB6A_amount = data.get("totalNutrients", {}).get("VITB6A", {"quantity": "0", "unit": "mg"})
            print(f"Vitamin B-6A: {vitB6A_amount["quantity"]} {vitB6A_amount["unit"]}")
            # Gets vitamin C data.
            vitC_amount = data.get("totalNutrients", {}).get("VITC", {"quantity": "0", "unit": "mg"})
            print(f"Vitamin C: {vitC_amount["quantity"]} {vitC_amount["unit"]}")
            # Gets vitamin D data.
            vitD_amount = data.get("totalNutrients", {}).get("VITD", {"quantity": "0", "unit": "N/A"})
            print(f"Vitamin D: {vitD_amount["quantity"]} {vitD_amount["unit"]}")
        else:
            print(f"Error {response.status_code}, {response.text}")
        return 0

