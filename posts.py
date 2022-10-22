from db import db
from datetime import datetime



def get_posts():
    try:
        sql= "SELECT id, title, content, user_id, visibility, TO_CHAR(created, \'HH24:MI, Mon dd yyyy\'), topic_id FROM posts"
        result=db.session.execute(sql)
        message=result.fetchall()
        return message
    except:
        return False


def get_posts_by_user(user_id):
    try:
        sql= "SELECT id, title, content, user_id, visibility, TO_CHAR(created, \'HH24:MI, Mon dd yyyy\'), topic_id FROM posts WHERE user_id = user_id"
        result=db.session.execute(sql, {"user_id":user_id})
        message=result.fetchall()
        return message
    except:
        return False

def get_posts_count_by_user(user_id):
    try:
        sql= "SELECT count(id) FROM posts WHERE user_id = user_id"
        result=db.session.execute(sql, {"user_id":user_id})
        message=result.fetchall()
        return message
    except:
        return False

def get_text_avg_by_user(user_id):
        sql= "SELECT ROUND(AVG(LENGTH(content)),0) FROM posts WHERE user_id = user_id"
        result=db.session.execute(sql, {"user_id":user_id})
        message=result.fetchone()
        return message
def create_post(title, content, visibility, user_id, topic_id):

        sql= "INSERT INTO posts (title, content, user_id, topic_id, visibility) VALUES (:title, :content, :user_id, :topic_id, :visibility)"
        db.session.execute(sql, {"title":title, "content":content, "user_id":user_id, "topic_id":topic_id, "visibility":visibility})
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


def get_post(post_id):
    try:
        sql= "SELECT * FROM posts WHERE id=:id"
        result=db.session.execute(sql, {"id":post_id})
        message=result.fetchone()
        return message
    except:
        return False




def get_topic(topic_id):
    try:
        sql= "SELECT topic FROM topics where id=:id"
        result=db.session.execute(sql, {"id":topic_id})
        message=result.fetchone()
        return message
    except:
        return False



def get_topics():
    try:
        sql= "SELECT id, topic FROM topics ORDER BY topic DESC"
        result=db.session.execute(sql)
        message=result.fetchall()
        return message
    except:
        return False


def get_comments(post_id):
    try:
        sql= "SELECT id, content, visibility, user_id, post_id, TO_CHAR(created, \'HH24:MI, Mon dd yyyy\') FROM comments WHERE post_id=:post_id"
        result=db.session.execute(sql, {"post_id":post_id})
        message=result.fetchall()
        return message
    except:
        return False


def get_all_comments():
    try:

        sql= "SELECT post_id, count(post_id) FROM comments WHERE visibility = TRUE GROUP BY post_id"
        result=db.session.execute(sql)
        message=result.fetchall()
        return message
    except:
        return False

def create_comment(content, visibility, user_id, post_id):

        sql= "INSERT INTO comments (content, user_id, post_id, visibility) VALUES (:content, :user_id, :post_id, :visibility)"
        db.session.execute(sql, {"content":content, "user_id":user_id, "post_id":post_id, "visibility":visibility})
        db.session.commit()
        return True


def create_topic(topic_name):

        sql= "INSERT INTO topics (topic) VALUES (:topic)"
        db.session.execute(sql, {"topic":topic_name})
        db.session.commit()
        return True


def delete_comment(comment_id):


        sql= "UPDATE comments SET visibility=FALSE WHERE id=:id"
        db.session.execute(sql, {"id":comment_id})
        db.session.commit()
        return True


def delete_topic(topic_id):


        sql= "delete FROM topics WHERE id=:id"
        db.session.execute(sql, {"id":topic_id})
        db.session.commit()
        return True

