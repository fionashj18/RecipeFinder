"""
Recipe generator backend — proxies requests to Spoonacular API.
Set SPOONACULAR_API_KEY in environment or .env file.
"""
import os
import requests
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static")
API_KEY = os.environ.get("SPOONACULAR_API_KEY")
COMPLEX_SEARCH = "https://api.spoonacular.com/recipes/complexSearch"

VALID_CUISINES = {
    "african", "american", "british", "cajun", "caribbean", "chinese",
    "eastern european", "french", "german", "greek", "indian", "irish",
    "italian", "japanese", "jewish", "korean", "latin american",
    "mediterranean", "mexican", "middle eastern", "nordic", "southern",
    "spanish", "thai", "vietnamese",
}


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/api/recipes")
def get_recipes():
    if not API_KEY:
        return jsonify({"error": "SPOONACULAR_API_KEY is not set"}), 500

    ingredients = request.args.get("ingredients", "").strip()
    if not ingredients:
        return jsonify({"error": "Provide at least one ingredient"}), 400

    number = request.args.get("number", "10")
    try:
        number = min(20, max(1, int(number)))
    except ValueError:
        number = 10

    cuisine = request.args.get("cuisine", "").strip().lower()
    vegan = request.args.get("vegan", "").lower() in ("true", "1", "yes")
    high_protein = request.args.get("high_protein", "").lower() in ("true", "1", "yes")
    high_fat = request.args.get("high_fat", "").lower() in ("true", "1", "yes")
    spicy = request.args.get("spicy", "").strip().lower()

    params = {
        "apiKey": API_KEY,
        "includeIngredients": ingredients,
        "number": number,
        "fillIngredients": "true",
        "addRecipeNutrition": "true",
        "sort": "max-used-ingredients",
    }

    if cuisine and cuisine in VALID_CUISINES:
        params["cuisine"] = cuisine
    if vegan:
        params["diet"] = "vegan"
    if high_protein:
        params["minProtein"] = 25
    if high_fat:
        params["minFat"] = 20
    if spicy and spicy in ("mild", "medium", "hot"):
        params["query"] = "spicy"

    try:
        r = requests.get(COMPLEX_SEARCH, params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
        return jsonify(data.get("results", []))
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 502


if __name__ == "__main__":
    app.run(debug=True, port=5000)
