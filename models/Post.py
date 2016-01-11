from . import dbfunctions as db

class Post:
    def __init__ (self, post_id, message, author_id, status, timestamp):
        self._post_id = post_id
        self._message = message
        self._author_id = author_id
        self._status = status
        self._timestamp = timestamp

    def __str__(self):
        return 'Object for post {} by {}'.format(self._message, self._author_id)



#********************************************************************************
#********************************************************************************
#Return fields
#********************************************************************************
#********************************************************************************

    def get_post_id(self):
        return self._post_id

    def get_message(self):
        return self._message

    def get_author_id(self):
        return self._author_id

    def get_status(self):
        return self._status

    def get_timestamp(self):
        return self._timestamp


    def get_recent_10(self):
        pass
        #return select(<recent 10 posts>)

    @classmethod
    def get_all_user_posts(klass, user_id):
        postList = []
        postData = db.select('post', 'author_id = %s' % user_id, 'post_id', 'message', 'author_id', 'status', 'timestamp')
        for line in postData:
            newPost = Post(line[0], line[1], line[2], line[3], line[4])
            postList.append(newPost)
        return postList

    @classmethod
    def get_all_posts(klass):
        postList = []
        postData = db.select('post', None, 'post_id', 'message', 'author_id', 'status', 'timestamp')
        for line in postData:
            newPost = Post(line[0], line[1], line[2], line[3], line[4])
            postList.append(newPost)
        return postList

    @classmethod
    def create_post(klass, columnvaluedict):
        inserted_id = db.insert('post', columnvaluedict)
        newPost = Post(inserted_id, columnvaluedict.get('message'), columnvaluedict.get('author_id'), columnvaluedict.get('status'), columnvaluedict.get('timestamp'))
        return newPost

    #def newPost(self, title, message, author, status):
    #def Post(self, title, message, author, status):

'''
    def updateTitle(self, newTitle):
        self.title = newTitle

    def updateMessage(self, newMessage):
        self.message = newMessage

    def updateStatus(self, newStatus):
        self.status = newStatus
'''



newPost = Post.create_post({
    'message': 'hello!',
    'author_id': 23,
    'status': 1,
    'timestamp': '35/1/10/2016'
})

print(Post.get_all_user_posts(2))
#print(Post.get_all_posts())
