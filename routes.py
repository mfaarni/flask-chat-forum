from app import app
import users, posts
from flask import render_template, request, redirect, session


@app.route("/")
def index():
    all_posts= posts.get_posts()
    if all_posts!=False:
        return render_template("index.html", all_posts=all_posts)
    else:
        return render_template("index.html")
 
@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password):
            return render_template("error.html", message="virheelliset kirjautumissyötteet")
        return redirect('/')

@app.route("/register",methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]
        if users.register(username, password, role):
            users.login(username, password)
        else:
            return render_template("error.html", message="rekisteröityminen epäonnistui")

        return redirect("/")



@app.route("/new_post",methods=["get", "post"])
def new():
    if request.method == "GET":
        return render_template("new_post.html")
        
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        id=request.form["user_id"]
        if not posts.create_post(title, content, id):
            return render_template("error.html", message="bruh")
        
        return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
