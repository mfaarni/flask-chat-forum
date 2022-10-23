from db import db


def get_posts():
    try:
        sql= '''
            SELECT DISTINCT p.id, p.title, p.content, p.user_id, p.visibility, TO_CHAR(p.created, \'HH24:MI, Mon dd yyyy\'), p.topic_id, t.topic
            FROM posts p, topics t
            WHERE visibility= TRUE AND p.topic_id = t.id AND topic_id IN (
            SELECT id FROM topics)
            ORDER BY p.id ASC
            '''
        result=db.session.execute(sql)
        message=result.fetchall()
        return message
    except:
        return False


def get_posts_by_user(user_id):
    try:
        sql= '''SELECT id, title, content, user_id, visibility, TO_CHAR(created, \'HH24:MI, Mon dd yyyy\'), topic_id 
                FROM posts 
                WHERE user_id = user_id'''
        result=db.session.execute(sql, {"user_id":user_id})
        message=result.fetchall()
        return message
    except:
        return False

def get_posts_count_by_user(user_id):
    try:
        sql= '''SELECT count(id) 
                FROM posts
                WHERE user_id = user_id'''
        result=db.session.execute(sql, {"user_id":user_id})
        message=result.fetchall()
        return message
    except:
        return False

def get_text_avg_by_user(user_id):
        sql= '''SELECT ROUND(AVG(LENGTH(content)),0) 
                FROM posts 
                WHERE user_id = user_id'''
        result=db.session.execute(sql, {"user_id":user_id})
        message=result.fetchone()

        return message

def create_post(title, content, visibility, user_id, topic_id):

        sql= '''INSERT INTO posts (title, content, user_id, topic_id, visibility) 
                VALUES (:title, :content, :user_id, :topic_id, :visibility) 
                RETURNING *
            '''
        sql2 = db.session.execute(sql, {"title":title, "content":content, "user_id":user_id, "topic_id":topic_id, "visibility":visibility})
        db.session.commit()
        sql3=sql2.fetchone()
        return str(sql3.id)
        
        


def delete_post(post_id):


        sql= '''UPDATE posts SET visibility=FALSE 
                WHERE id=:id'''
        db.session.execute(sql, {"id":post_id})
        db.session.commit()
        return True



def get_title(post_id):
    try:
        sql= '''SELECT title 
                FROM posts 
                WHERE id=:id'''
        result=db.session.execute(sql, {"id":post_id})
        message=result.fetchone()
        return message
    except:
        return False

def get_content(post_id):
    try:
        sql= '''SELECT content  
                FROM posts 
                WHERE id=:id'''
        result=db.session.execute(sql, {"id":post_id})
        message=result.fetchone()
        return message
    except:
        return False


def get_post(post_id):
    try:
        sql= '''SELECT id, title, content, user_id, visibility, TO_CHAR(created, \'HH24:MI, Mon dd yyyy\'), topic_id 
                FROM posts 
                WHERE id=:id'''
        result=db.session.execute(sql, {"id":post_id})
        message=result.fetchone()
        return message
    except:
        return False



def get_random_post():
    try:
        sql= '''SELECT id 
                FROM posts 
                WHERE visibility = TRUE AND topic_id IN (SELECT id FROM topics)
                ORDER BY RANDOM() 
                LIMIT 1'''
        result=db.session.execute(sql)
        message=result.fetchone()
        return message
    except:
        return False


