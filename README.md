# Recipe Generator

Minimal web app that finds recipes based on ingredients you have, using the [Spoonacular API](https://spoonacular.com/food-api).

## Setup

1. **Get an API key** (free tier available): [Spoonacular Food API](https://spoonacular.com/food-api/console)

2. **Create a `.env` file** in this folder:

   ```
   SPOONACULAR_API_KEY=your_api_key_here
   ```

3. **Install dependencies and run:**

   ```bash
   pip install -r requirements.txt
   python app.py
   ```

4. Open **http://127.0.0.1:5000** in your browser.

## Usage

Type one or more ingredients (comma-separated), e.g. `chicken, rice, tomato`, and click **Find recipes**. Results show what you have vs what you’d need; click a recipe to open it on Spoonacular.
