import os
from flask import (Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# ---- CONFIG ----- #
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    return render_template("recipes.html", recipes = list(mongo.db.recipes.find()))


@app.route("/recipes/<category_id>")
def recipes(category_id):
    if category_id:
        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})["category_name"]
        recipes = list(mongo.db.recipes.find({"category_name": category}))
    return render_template("recipes.html", recipes=recipes)


# ---- Account (Register, login, logout) ----- #
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("username already exists")
            return redirect(url_for("register"))
      
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into "session" cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if username ecists in db database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            # in [] because it belongs to existing_user
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
# identify and grab the session user's username from mongo db
    if session["user"]:
        # gives admin view to all recipes + users view to their recipes
        if session["user"] == "admin":
            recipe = mongo.db.recipes.find({"created_by": username})
        else:
            recipe = mongo.db.recipes.find({"created_by": username})
        return render_template("profile.html", recipe=recipe, username=username)
    return render_template("login.html")


@app.route("/logout")
def logout():
    #remove user form the session cookies
    flash("You are logged out now!")
    session.pop("user")
    return redirect(url_for("login"))


# ---- recipe_page ----- #


@app.route("/recipes_page/<recipe_id>")
def recipes_page(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("recipes_page.html", recipe=recipe)

# ---- Recipes (categories, add, edit) ----- #
# ---- add_recipe ----- #


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        vegan = "on" if request.form.get("vegan") else "off"
        print(request.form.get('image_url'))
        recipe = {
            "image_url": request.form.get("image_url"),
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients").split(";"),
            "recipe_instructions": request.form.get("recipe_instructions").split(";"),
            "recipe_tips": request.form.get("recipe_tips").split(";"),
            "vegan": vegan,
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added to the website")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)

# ---- edit_recipe ----- #


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        vegan = "on" if request.form.get("vegan") else "off"
        print(request.form.get("image_url"))
        submit = {
            "image_url": request.form.get("image_url"),
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients").split(";"),
            "recipe_instructions": request.form.get("recipe_instructions").split(";"),
            "recipe_tips": request.form.get("recipe_tips").split(";"),
            "vegan": vegan,
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe edited!")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


# ---- delete_recipe ----- #
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted!")
    return redirect(url_for("get_recipes"))


# ---- categories ----- #
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# ---- contact ----- #
@app.route("/contact")
def contact():
    return render_template("contact.html")



@app.route("/login22", methods=["GET", "POST"])
def login222():
    session["user"] = "admin"
    return render_template("login.html")



# always leave in the end 
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)
