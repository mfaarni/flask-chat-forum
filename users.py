from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash


def login(username, password):
    hash_value = generate_password_hash(password)
    sql = "SELECT id, password, role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        session['id']=user[0]
        session['username'] = username
        session["role"]=user[2]
        if check_password_hash(hash_value, password):
            return True
        return False


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
    else:
        return False
    return login(username, password)
