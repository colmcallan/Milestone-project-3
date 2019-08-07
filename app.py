import os
import math
import re
from flask_pymongo import PyMongo, pymongo
from forms import RecipeForm
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from flask import (Flask, render_template, redirect,
                   request, url_for, flash, session)
app = Flask(__name__)
recipies = list(range(100))
# connecting to the database

app.config["MONGO_DBNAME"] = "cookbook_creation"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "monogodb://localhost")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

# results per page for pagination
def get_recipies(offset=0, per_page=5):
    return mongo.db.all_recipes.find()[offset: offset + per_page]

#search recipes
def search_recipies(offset=0, per_page=5, search_term=''):
    return mongo.db.all_recipes.find({'recipe': {'$regex': search_term}}) [offset: offset + per_page]

# username only login at first connection of site

 
@app.route("/", methods=["GET", "POST"])
def login():
    """Main page with login"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("get_meals", username=session["username"]))

    return render_template("login.html")
# redirects to index once complete

@app.route("/login/<username>", methods=["GET", "POST"])
def user(username):
    if request.method == "POST":
        username = session["username"]
        return redirect(url_for("user", username=session["username"]))
    return render_template("index.html", username=username)


# index screen, paginated to show 5 results per page. displaying all recipes. 
@app.route('/all_view')
def all_view():
    page = int(request.args.get('page', 1))
    per_page = 10
    offset = (page - 1) * per_page
    paginated_recipies = get_recipies(offset=offset, per_page=per_page)
    total=paginated_recipies.count()
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    
    return render_template('allrecipes.html',
                            recipies=paginated_recipies,
                            page=page,
                            per_page=per_page,
                            pagination=pagination)

#searchfunction
@app.route('/search/')
def search_view():
    page = int(request.args.get('page', 1))
    per_page = 2
    offset = (page - 1) * per_page
    search_query = request.args.get('search_box')
    paginated_recipies = search_recipies(offset=offset, per_page=per_page, search_term=search_query)
    total=paginated_recipies.count()
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    
    return render_template('results.html',
                            recipies=paginated_recipies,
                            page=page,
                            per_page=per_page,
                            pagination=pagination)
                            


# function to add meal type to the website                            

@app.route('/add_meal')
def add_meal():
    return render_template('addmeal.html',
                            all_recipes = mongo.db.all_recipes.find())
# route back to index           
@app.route('/get_meals')
def get_meals():
    return render_template('index.html')

# function to add recipes to the website                            


@app.route('/insert_meal', methods=['POST'])
def insert_meal():
    all_recipes = mongo.db.all_recipes
    
    all_recipes.insert_one(request.form.to_dict())
    
    return redirect(url_for('get_meals'))

# function to edit recipe form and push this edit through to

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    _recipe = mongo.db.all_recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe= _recipe)
    

@app.route('/update_recipe/<recipe_id>', methods=['GET', 'POST'])
def update_recipe(recipe_id):
    all_recipes = mongo.db.all_recipes
    
    all_recipes.update( {'_id': ObjectId(recipe_id)},
    { 
            'recipe': request.form['recipe_name'],
            'recipe_name': request.form['recipe_name'],
            'recipe_image': request.form['recipe_image'],
            'serving_size': int(request.form['serving_size']),
            'diet_labels': request.form['diet_labels'],
            'health_labels': request.form['health_labels'],
            'ingredients': request.form['ingredients'],
            'calories': request.form['calories'],
            'cooking_time': request.form['cooking_time'],
            'description': request.form['description'],
            'method': request.form['method']
                })
    return redirect(url_for('get_meals'))
    


# function to show the recipe that the user clicks on    
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    return render_template('recipe.html',
    recipe=mongo.db.all_recipes.find_one({'_id': ObjectId(recipe_id)}))
    
# function to delete recipes from the website

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    
    mongo.db.all_recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_meals'))
    
@app.route('/store')
def store():
    return render_template('store.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
            port=int(os.environ.get('PORT')),
            debug=False)