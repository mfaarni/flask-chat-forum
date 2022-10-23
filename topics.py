from db import db



def get_topic(topic_id):
    try:
        sql= '''SELECT topic 
                FROM topics 
                WHERE id=:id'''
        result=db.session.execute(sql, {"id":topic_id})
        message=result.fetchone()
        return message
    except:
        return False



def get_topics():
    try:
        sql= '''SELECT id, topic 
                FROM topics 
                ORDER BY topic DESC'''
        result=db.session.execute(sql)
        message=result.fetchall()
        return message
    except:
        return False


def create_topic(topic_name):

        sql= '''INSERT INTO topics (topic) 
                VALUES (:topic)'''
        db.session.execute(sql, {"topic":topic_name})
        db.session.commit()
        return True



def delete_topic(topic_id):


        sql= '''delete 
                FROM topics 
                WHERE id=:id'''
        db.session.execute(sql, {"id":topic_id})
        db.session.commit()
        return True

