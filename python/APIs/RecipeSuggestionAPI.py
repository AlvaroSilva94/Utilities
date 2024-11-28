from flask import Flask, request, jsonify

app = Flask(__name__)

recipes = [
{
        'id': 1,
        'name': 'Pasta Carbonara',
        'ingredients': ['pasta', 'eggs', 'bacon', 'parmesan cheese'],
        'category': 'Italian',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 2,
        'name': 'Veggie Stir-Fry',
        'ingredients': ['tofu', 'broccoli', 'carrots', 'bell peppers'],
        'category': 'Asian',
        'diet': 'Vegetarian'
    },
    {
        'id': 3,
        'name': 'Grilled Salmon',
        'ingredients': ['salmon', 'lemon', 'olive oil', 'dill'],
        'category': 'Seafood',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 4,
        'name': 'Chicken Tikka Masala',
        'ingredients': ['chicken', 'tomatoes', 'yogurt', 'garam masala'],
        'category': 'Indian',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 5,
        'name': 'Caprese Salad',
        'ingredients': ['tomatoes', 'mozzarella', 'basil', 'balsamic vinegar'],
        'category': 'Salad',
        'diet': 'Vegetarian'
    },
    {
        'id': 6,
        'name': 'Beef Tacos',
        'ingredients': ['beef', 'tortillas', 'lettuce', 'cheese'],
        'category': 'Mexican',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 7,
        'name': 'Mushroom Risotto',
        'ingredients': ['mushrooms', 'arborio rice', 'vegetable broth', 'parmesan cheese'],
        'category': 'Italian',
        'diet': 'Vegetarian'
    },
    {
        'id': 8,
        'name': 'Lemon Herb Roast Chicken',
        'ingredients': ['chicken', 'lemon', 'garlic', 'rosemary'],
        'category': 'Roast',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 9,
        'name': 'Shrimp Pad Thai',
        'ingredients': ['shrimp', 'rice noodles', 'eggs', 'peanuts'],
        'category': 'Thai',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 10,
        'name': 'Vegetable Curry',
        'ingredients': ['mixed vegetables', 'coconut milk', 'curry paste'],
        'category': 'Indian',
        'diet': 'Vegetarian'
    },
    {
        'id': 11,
        'name': 'Baked Ziti',
        'ingredients': ['ziti pasta', 'tomato sauce', 'ricotta cheese', 'mozzarella cheese'],
        'category': 'Italian',
        'diet': 'Vegetarian'
    },
    {
        'id': 12,
        'name': 'Teriyaki Salmon',
        'ingredients': ['salmon', 'soy sauce', 'ginger', 'honey'],
        'category': 'Seafood',
        'diet': 'Non-Vegetarian'
    },
        {
        'id': 13,
        'name': 'Chicken Parmesan',
        'ingredients': ['chicken breast', 'breadcrumbs', 'tomato sauce', 'mozzarella cheese'],
        'category': 'Italian',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 14,
        'name': 'Sushi Rolls',
        'ingredients': ['sushi rice', 'nori seaweed', 'avocado', 'fish'],
        'category': 'Japanese',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 15,
        'name': 'Spinach and Feta Stuffed Chicken Breast',
        'ingredients': ['chicken breast', 'spinach', 'feta cheese', 'garlic'],
        'category': 'Stuffed',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 16,
        'name': 'Quinoa Salad',
        'ingredients': ['quinoa', 'cucumber', 'tomatoes', 'feta cheese'],
        'category': 'Salad',
        'diet': 'Vegetarian'
    },
    {
        'id': 17,
        'name': 'BBQ Pulled Pork Sandwiches',
        'ingredients': ['pork shoulder', 'barbecue sauce', 'buns', 'coleslaw'],
        'category': 'Sandwich',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 18,
        'name': 'Egg Fried Rice',
        'ingredients': ['rice', 'eggs', 'vegetables', 'soy sauce'],
        'category': 'Asian',
        'diet': 'Vegetarian'
    },
    {
        'id': 19,
        'name': 'Roasted Vegetable Medley',
        'ingredients': ['carrots', 'potatoes', 'zucchini', 'bell peppers'],
        'category': 'Roast',
        'diet': 'Vegetarian'
    },
    {
        'id': 20,
        'name': 'Baked Honey Mustard Salmon',
        'ingredients': ['salmon', 'honey', 'mustard', 'dijon mustard'],
        'category': 'Seafood',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 21,
        'name': 'Mediterranean Quinoa Bowl',
        'ingredients': ['quinoa', 'chickpeas', 'cucumber', 'feta cheese'],
        'category': 'Salad',
        'diet': 'Vegetarian'
    },
    {
        'id': 22,
        'name': 'Thai Green Curry',
        'ingredients': ['chicken', 'green curry paste', 'coconut milk', 'vegetables'],
        'category': 'Thai',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 23,
        'name': 'Caprese Pizza',
        'ingredients': ['pizza dough', 'tomatoes', 'mozzarella cheese', 'basil'],
        'category': 'Italian',
        'diet': 'Vegetarian'
    },
    {
        'id': 24,
        'name': 'Honey Sesame Chicken',
        'ingredients': ['chicken', 'soy sauce', 'honey', 'sesame seeds'],
        'category': 'Asian',
        'diet': 'Non-Vegetarian'
    },
        {
        'id': 25,
        'name': 'Crispy Baked Chicken Wings',
        'ingredients': ['chicken wings', 'flour', 'spices', 'barbecue sauce'],
        'category': 'Appetizer',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 26,
        'name': 'Vegetable Lasagna',
        'ingredients': ['lasagna noodles', 'vegetables', 'tomato sauce', 'ricotta cheese'],
        'category': 'Italian',
        'diet': 'Vegetarian'
    },
    {
        'id': 27,
        'name': 'Garden Salad',
        'ingredients': ['lettuce', 'tomatoes', 'cucumber', 'olives'],
        'category': 'Salad',
        'diet': 'Vegetarian'
    },
    {
        'id': 28,
        'name': 'Steak with Chimichurri Sauce',
        'ingredients': ['steak', 'parsley', 'garlic', 'red wine vinegar'],
        'category': 'Steak',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 29,
        'name': 'Vegetable Spring Rolls',
        'ingredients': ['spring roll wrappers', 'cabbage', 'carrots', 'soy sauce'],
        'category': 'Asian',
        'diet': 'Vegetarian'
    },
    {
        'id': 30,
        'name': 'Lemon Bars',
        'ingredients': ['butter', 'sugar', 'lemons', 'flour'],
        'category': 'Dessert',
        'diet': 'Vegetarian'
    },
    {
        'id': 31,
        'name': 'Chicken Parmesan',
        'ingredients': ['chicken breasts', 'bread crumbs', 'tomato sauce', 'mozzarella cheese'],
        'category': 'Italian',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 32,
        'name': 'Spinach and Feta Stuffed Mushrooms',
        'ingredients': ['mushrooms', 'spinach', 'feta cheese', 'garlic'],
        'category': 'Appetizer',
        'diet': 'Vegetarian'
    },
    {
        'id': 33,
        'name': 'Miso Soup',
        'ingredients': ['miso paste', 'tofu', 'seaweed', 'green onions'],
        'category': 'Soup',
        'diet': 'Vegetarian'
    },
    {
        'id': 34,
        'name': 'Teriyaki Salmon',
        'ingredients': ['salmon fillets', 'teriyaki sauce', 'ginger', 'garlic'],
        'category': 'Seafood',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 35,
        'name': 'Caprese Salad',
        'ingredients': ['tomatoes', 'mozzarella cheese', 'basil leaves', 'balsamic glaze'],
        'category': 'Salad',
        'diet': 'Vegetarian'
    },
    {
        'id': 36,
        'name': 'Honey Mustard Chicken',
        'ingredients': ['chicken breasts', 'honey', 'mustard', 'lemon juice'],
        'category': 'Chicken',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 37,
        'name': 'Pineapple Fried Rice',
        'ingredients': ['rice', 'pineapple', 'shrimp', 'vegetables'],
        'category': 'Asian',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 38,
        'name': 'Vegetable Curry',
        'ingredients': ['mixed vegetables', 'coconut milk', 'curry paste', 'spices'],
        'category': 'Curry',
        'diet': 'Vegetarian'
    },
    {
        'id': 39,
        'name': 'Beef Tacos',
        'ingredients': ['beef', 'taco shells', 'lettuce', 'salsa'],
        'category': 'Mexican',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 40,
        'name': 'Ratatouille',
        'ingredients': ['eggplant', 'zucchini', 'tomatoes', 'bell peppers'],
        'category': 'Vegetarian',
        'diet': 'Vegetarian'
    },
    {
        'id': 41,
        'name': 'Stuffed Bell Peppers',
        'ingredients': ['bell peppers', 'rice', 'ground beef', 'tomato sauce'],
        'category': 'Vegetarian',
        'diet': 'Non-Vegetarian'
    },
    {
        'id': 42,
        'name': 'Homemade Pizza',
        'ingredients': ['pizza dough', 'tomato sauce', 'cheese', 'toppings'],
        'category': 'Italian',
        'diet': 'Vegetarian'
    }
]

@app.route('/recipes', methods=['POST'])
def get_recipe_recommendations():
    data = request.json
    dietary_preference = data.get('dietary_preference')
    ingredients = data.get('ingredients')
    cooking_preference = data.get('cooking_preference')

    recommended_recipes = []

    for recipe in recipes:
        if (not dietary_preference or recipe['diet'] == dietary_preference) and \
                (not ingredients or all(ingredient in recipe['ingredients'] for ingredient in ingredients)) and \
                (not cooking_preference or recipe['category'] == cooking_preference):
            recommended_recipes.append(recipe)

    return jsonify({'recipes': recommended_recipes})

if __name__ == '__main__':
    app.run(debug=True)