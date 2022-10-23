from db import db

def get_comments(post_id):
    try:
        sql= '''SELECT id, content, visibility, user_id, post_id, TO_CHAR(created, \'HH24:MI, Mon dd yyyy\') 
                FROM comments 
                WHERE post_id=:post_id'''
        result=db.session.execute(sql, {"post_id":post_id})
        message=result.fetchall()
        return message
    except:
        return False


def get_all_comments():
    try:

        sql= '''SELECT post_id, count(post_id) 
                FROM comments 
                WHERE visibility = TRUE 
                GROUP BY post_id'''
        result=db.session.execute(sql)
        message=result.fetchall()
        return message
    except:
        return False

def create_comment(content, visibility, user_id, post_id):

        sql= '''INSERT INTO comments (content, user_id, post_id, visibility) 
                VALUES (:content, :user_id, :post_id, :visibility)'''
        db.session.execute(sql, {"content":content, "user_id":user_id, "post_id":post_id, "visibility":visibility})
        db.session.commit()
        return True


def delete_comment(comment_id):


        sql= '''UPDATE comments 
                SET visibility=FALSE 
                WHERE id=:id'''
        db.session.execute(sql, {"id":comment_id})
        db.session.commit()
        return True
