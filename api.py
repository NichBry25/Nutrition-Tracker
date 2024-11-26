import requests

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
            # Gets carbohydates data.
            carbs_amount = data.get("totalNutrients", {}).get("CHOCDF.net", {"quantity": "0", "unit": "g"})
            # Gets cholesteorol data.
            chole_amount = data.get("totalNutrients", {}).get("CHOLE", {"quantity": "0", "unit": "mg"})
            # Gets fats data.
            fat_amount = data.get("totalNutrients", {}).get("FAT", {"quantity": "0", "unit": "g"})
            # Gets protein data.
            protein_amount = data.get("totalNutrients", {}).get("PROCNT", {"quantity": "0", "unit": "g"})
            # Gets sodium data.
            sodium_amount = data.get("totalNutrients", {}).get("NA", {"quantity": "0", "unit": "mg"})
            # Gets calcium data.
            calcium_amount = data.get("totalNutrients", {}).get("CA", {"quantity": "0", "unit": "mg"})
            # Gets iron data.
            iron_amount = data.get("totalNutrients", {}).get("FE", {"quantity": "0", "unit": "mg"})
            # Gets potassium data.
            potas_amount = data.get("totalNutrients", {}).get("K", {"quantity": "0", "unit": "mg"})
            # Gets vitamin B12 data.
            vitB12_amount = data.get("totalNutrients", {}).get("VITB12", {"quantity": "0", "unit": "N/A"})
            # Gets vitamin B6A data.
            vitB6A_amount = data.get("totalNutrients", {}).get("VITB6A", {"quantity": "0", "unit": "mg"})
            # Gets vitamin C data.
            vitC_amount = data.get("totalNutrients", {}).get("VITC", {"quantity": "0", "unit": "mg"})
            # Gets vitamin D data.
            vitD_amount = data.get("totalNutrients", {}).get("VITD", {"quantity": "0", "unit": "N/A"})

        else:
            print(f"Error {response.status_code}, {response.text}")

        return {
                "calories_from_API": calories_amount["quantity"],
                "carbohydrates_from_API": carbs_amount["quantity"],
                "cholesterol_from_API": chole_amount["quantity"],
                "fat_from_API": fat_amount["quantity"],
                "protein_from_API": protein_amount["quantity"],
                "sodium_from_API": sodium_amount["quantity"],
                "calcium_from_API": calcium_amount["quantity"],
                "iron_from_API": iron_amount["quantity"],
                "potassium_from_API": potas_amount["quantity"],
                "vitb12_from_API": vitB12_amount["quantity"],
                "vitb6a_from_API": vitB6A_amount["quantity"],
                "vitc_from_API": vitC_amount["quantity"],
                "vitd_from_API": vitD_amount["quantity"]
            }
