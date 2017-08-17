from pymongo import MongoClient
import datetime

post = {"author": "lmpizarro",
        "text": "my second blog post!",
        "tags": ["mongodb"],
        "date": datetime.datetime.utcnow()}



class connMDB(object):

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.test_database
        self.posts = self.db.posts # a collection

class myApp01DB (object):

    def __init__(self):

        self.conn = connMDB()

    def getAll(self):

        tquery = []
        query_all  = self.conn.posts.find()

        for q in query_all:
            tquery.append(q)

        return tquery

    def inserOne (self, post):

        post_id = self.conn.posts.insert_one(post).inserted_id

DbConn = myApp01DB()
