from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId


post = {"author": "lmpizarro",
        "text": "my second blog post!",
        "tags": ["mongodb"],
        "date": datetime.datetime.utcnow()}

'''
    See:
        https://www.freelancer.co.it/community/articles/crud-operations-in-mongodb-using-python
'''
class Post (object):

    def __init__(self, post_id=None, text=None, tags=None, author=None, \
                date= None):

        if post_id is None:
            self._id = ObjectId()
        else:
            self._id = post_id

        self.author = author
        self.text = text
        self.tags=tags
        if date is None: 
            self.date = datetime.datetime.utcnow()
        else:
            self.date = date



    def getJson(self):
        """ Method returns the JSON representation of the
            Project object, which can be saved to MongoDB 
        """
        return self.__dict__

    @staticmethod    
    def build_from_json(json_data):
        """ Method used to build Project objects from JSON data returned from MongoDB """
        if json_data is not None:
            try:                            
                return Post(json_data.get('_id', None),
                    json_data['text'],
                    json_data['tags'],
                    json_data['author'],
                    json_data['date'])
            except KeyError as e:
                raise Exception("Key not found in json_data: {}".format(e.message))
        else:
            raise Exception("No data to create Project from!")

    def __str__(self):
        format_ = ("author: %s post: %s \n")
        str_ = format_ % (self.author, self.text)
        return str_ 


class connMDB(object):

    def __init__(self, host=None, port=None, database=None):
        if host == None and port == None and database == None: 
            self.client = MongoClient(host="localhost", port=27017)
            self.db = self.client.test_database
            self.posts = self.db.posts # a collection
        else:
            raise Exception("Yet Not implemented!")


class myApp01DB (object):

    def __init__(self):

        self.conn = connMDB()


    def insertOne (self, post):
        if post is not None:
            post_id = self.conn.posts.insert_one(post).inserted_id
        else:
            raise Exception("Nothing to save, because project \
                                parameter is None")

    def getAll(self):
        return self.conn.posts.find()

    def getAuthor(self, author):
        return self.conn.posts.find({"author": author})

    '''
        tag is a []
    '''
    def getTag(self, tag):
        return self.conn.posts.find({"tags": tag})



DbConn = myApp01DB()

def test_insert():
    global post 
    global DbConn


    post["author"] = "pepe"
    post["text"] = "just another beuty post"
    post["tags"] = "test"

    DbConn.insertOne(post)

def test_Post():
    global DbConn
    pst = Post(author="pepe", text="otro post para probar post", \
            tags=["posts", "tests"])

    #DbConn.insertOne(pst.getJson())

    print pst.build_from_json(pst.getJson())

def test_getAll():    
    global DbConn
    query_all = DbConn.getAll()

    tq= []
    for q in query_all:
        tq.append(q)

        print q    

def test_getAuthor():    
    global DbConn
    query_all = DbConn.getAuthor("lmpizarro")

    tq= []
    for q in query_all:
        tq.append(q)

        print q    


def test_getTag():    
    global DbConn
    query_all = DbConn.getTag("test")

    tq= []
    for q in query_all:
        tq.append(q)

        print q    



if __name__ == '__main__':
    #test_Post()
    #test_Post()
    #test_getAuthor()
    test_getTag()
