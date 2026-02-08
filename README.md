Recipe Generator

Minimal web app that finds recipes based on ingredients you have, using the Spoonacular API(https://spoonacular.com/food-api). You can chose a specific cusine, spice level, vegan, high protein, and high fat. Each recipe will also tell you the macros of the meal.
 Key parameters sent to the API include ingredients the user has. The API returns JSON with recipes, that have descriptions of the name of the dish, the image, ingredients used, missing ingrediends, and macros per serving. 
I obtained the API key by signing up at Spoonacular Food API Console(https://spoonacular.com/food-api/console), create an account, and copied the API key from the dashboard. It is stored in the file `.env`. 
