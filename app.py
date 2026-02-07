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
BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"


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

    params = {
        "apiKey": API_KEY,
        "ingredients": ingredients,
        "number": number,
        "ranking": 1,  # maximize used ingredients
    }

    try:
        r = requests.get(BASE_URL, params=params, timeout=15)
        r.raise_for_status()
        return jsonify(r.json())
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 502


if __name__ == "__main__":
    app.run(debug=True, port=5000)
