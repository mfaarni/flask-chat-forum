from db import db
from datetime import datetime
import users




def get_posts():
    try:
        sql= "SELECT title, content, user_id, created FROM posts"
        result=db.session.execute(sql)
        message=result.fetchall()
        return message

    except:
        return False

def create_post(title, content, user_id):

        now=datetime.now()
        time=now.strftime("%d/%m/%Y %H:%M:%S")
        sql= "INSERT INTO posts (title, content, user_id, created) VALUES (:title, :content, :user_id, :created)"
        db.session.execute(sql, {"title":title, "content":content, "user_id":user_id, "created": time})
        db.session.commit()
        return True