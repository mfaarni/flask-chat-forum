from db import db
from datetime import datetime
import users




def get_posts():
    try:
        sql= "SELECT id, title, content, user_id, visibility, created FROM posts"
        result=db.session.execute(sql)
        message=result.fetchall()
        return message
    except:
        return False

def create_post(title, content, visibility, user_id):

        now=datetime.now()
        time=now.strftime("%d/%m/%Y %H:%M:%S")
        sql= "INSERT INTO posts (title, content, user_id, visibility, created) VALUES (:title, :content, :user_id, :visibility, :created)"
        db.session.execute(sql, {"title":title, "content":content, "user_id":user_id, "visibility":visibility, "created": time})
        db.session.commit()
        return True


def delete_post(post_id):


        sql= "UPDATE posts SET visibility=FALSE WHERE id=:id"
        db.session.execute(sql, {"id":post_id})
        db.session.commit()
        return True



def get_title(post_id):
    try:
        sql= "SELECT title FROM posts WHERE id=:id"
        result=db.session.execute(sql, {"id":post_id})
        message=result.fetchone()
        return message
    except:
        return False

def get_content(post_id):
    try:
        sql= "SELECT content FROM posts WHERE id=:id"
        result=db.session.execute(sql, {"id":post_id})
        message=result.fetchone()
        return message
    except:
        return False





def get_comments(post_id):
    try:
        sql= "SELECT id, content, visibility, user_id, post_id, created FROM comments WHERE post_id=:post_id"
        result=db.session.execute(sql, {"post_id":post_id})
        message=result.fetchall()
        return message
    except:
        return False

def create_comment(content, visibility, user_id, post_id):

        now=datetime.now()
        time=now.strftime("%d/%m/%Y %H:%M:%S")
        sql= "INSERT INTO comments (content, user_id, post_id, visibility, created) VALUES (:content, :user_id, :post_id, :visibility, :created)"
        db.session.execute(sql, {"content":content, "user_id":user_id, "post_id":post_id, "visibility":visibility, "created": time})
        db.session.commit()
        return True


def delete_comment(comment_id):


        sql= "UPDATE comments SET visibility=FALSE WHERE id=:id"
        db.session.execute(sql, {"id":comment_id})
        db.session.commit()
        return True

