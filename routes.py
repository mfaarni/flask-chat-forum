from app import app
import users, posts
from flask import render_template, request, redirect, session


@app.route("/")
def index():
    all_posts= posts.get_posts()
    quotes=users.get_quotes()
    if all_posts!=False:
        return render_template("index.html", all_posts=all_posts, quotes=quotes)
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
            return render_template("error.html", message="Käyttäjätunnusta ei löytynyt näillä arvoilla.")
        else:
            users.login(username, password)
            return redirect('/')

@app.route("/register",methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")


    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]
        if len(username)<3 or len(username)>14:
            return render_template("error.html", message="Käyttäjätunnuksen pitää olla 3-14 merkkiä pitkä.")
        if len(password)<3:
            return render_template("error.html", message="salasanan pituus tulee olla vähintään 3 merkkiä.")
        if " " in password:
            return render_template("error.html", message="Salasana ei saa sisältää välilyöntejä.")
        if " " in username or " " in password:
            return render_template("error.html", message="Käyttäjätunnus ei saa sisältää välilyöntejä.")
        else:
            if users.register(username, password, role):
                users.login(username, password)
            else:
                return render_template("error.html", message="Rekisteröityminen epäonnistui")

        return redirect("/")



@app.route("/new_post",methods=["get", "post"])
def new_post():
    if request.method == "GET":
        quote=users.get_quote()
        topics=posts.get_topics()
        if quote:
            return render_template("new_post.html", quote=quote, topics=topics)
        else:
            return render_template("new_post.html", topics=topics)

        
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if session["csrf_token"] != request.form["csrf_token"]:
            render_template("error.html", (403))
        id=request.form["user_id"]
        if not posts.create_post(title, content, True, id):
            return render_template("error.html", message="bruh")
        
        return redirect("/")

@app.route("/post/<post_id>")
def post_page(post_id):
    title=posts.get_title(post_id)
    content=posts.get_content(post_id)
    comments=posts.get_comments(post_id)
    post=posts.get_post(post_id)
    return render_template("/post.html", title = title, content = content, comments= comments, post=post, post_id=post_id)




@app.route("/quote",methods=["get", "post"])
def new_quote():
    if request.method == "GET":
        return render_template("quote.html")
        
    if request.method == "POST":
        content = request.form["content"]
        user_id=request.form["user_id"]
        if session["csrf_token"] != request.form["csrf_token"]:
            render_template("error.html", (403))

        if not users.set_quote(user_id, content):
            return render_template("error.html", message="quote not set")

        return redirect("/")

@app.route("/delete_post",methods=["get", "post"])
def delete_post():
    message_id = request.form["post_id"]
    try:
        posts.delete_post(message_id)
    except:
        return render_template("error.html", message="ei onnaa bro")
        
    return redirect("/")


@app.route("/new_comment",methods=["get", "post"])
def new_comment():
        content = request.form["content"]
        user_id=request.form["user_id"]
        post_id=request.form["post_id"]
        if not posts.create_comment(content, True, user_id, post_id):
            return render_template("error.html", message="bruh")
        
        return redirect("/post/"+post_id)


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

