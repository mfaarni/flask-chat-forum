from db import db
from flask import session, abort, request
from werkzeug.security import check_password_hash, generate_password_hash
import secrets


def login(username, password):
    sql = "SELECT id, password, role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False

    if not check_password_hash(user[1], password):
        return False
    else:

        session['id']=user[0]
        session['username'] = username
        session["role"]=user[2]
        session["csrf_token"] = secrets.token_hex(16)

        sql = "SELECT content FROM quotes WHERE user_id=:id"
        result = db.session.execute(sql, {"id":user[0]})
        user = result.fetchone()
        if user:
            session["quote"]=user[0]
        return True

def register(username, password, role):
    hash_value=generate_password_hash(password)
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if not user:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username, password, role) VALUES (:username, :password, :role)"
        db.session.execute(sql, {"username":username, "password":hash_value, "role":role})
        db.session.commit()
        return login(username, password)
    else:
        return False


def set_quote(user_id, new_content):
    sql = "SELECT content, user_id FROM quotes WHERE user_id=:user_id"
    result = db.session.execute(sql, {"user_id":user_id})
    user = result.fetchone()
    try:
        if not user:
                sql = "INSERT INTO quotes (content, user_id) VALUES (:content, :user_id)"
                db.session.execute(sql, {"content":new_content, "user_id":user_id})
                db.session.commit()
                session["quote"]=new_content
                return True
        else:
                sql= "UPDATE quotes SET content=:new_content WHERE user_id=:user_id"
                db.session.execute(sql, {"new_content":new_content, "user_id":user_id})
                db.session.commit()
                session["quote"]=new_content
                return True
    except:
        return False


def get_usernames():
    try:
        sql = '''SELECT id, username FROM users GROUP BY id'''
        result = db.session.execute(sql)
        message = result.fetchall()
        return message
    except:
        return False
def get_quote():
    try:
        user_id=session.id
        sql= "SELECT content, user_id FROM quotes where user_id=:user_id"
        result=db.session.execute(sql, {"user_id":user_id})
        message=result.fetchall()
        return message
    except:
        return False


def get_quote_id(user_id):
    try:
        sql= "SELECT content, user_id FROM quotes where user_id=:user_id"
        result=db.session.execute(sql, {"user_id":user_id})
        message=result.fetchall()
        return message
    except:
        return False




def get_quotes():
    try:
        sql= "SELECT content, user_id FROM quotes"
        result=db.session.execute(sql)
        message=result.fetchall()
        return message
    except:
        return False

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)