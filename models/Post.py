import dbfunctions as db

class Post:
	def __init__ (self, post_id, message, author_id, status, timestamp):
		self._post_id = post_id
		self._message = message
		self._author_id = author_id
		self._status = status
		self._timestamp = timestamp

	def __str__(self):
		return 'Obect for post {} by {}'.format(self.title, self.author)

	

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
	def get_all_user_posts(user_id):
		return db.select('post', 'author_id = %s' % user_id, '*')

	@classmethod
	def get_all_posts():
		   results = db.select('post', '', '*')
		   return results

	@classmethod
	def create_post(klass, columnvaluedict):
	   	db.insert('post', columnvaluedict)

	#def newPost(self, title, message, author, status):
	#def Post(self, title, message, author, status):


	def updateTitle(self, newTitle):
		self.title = newTitle
	
	def updateMessage(self, newMessage):
		self.message = newMessage

	def updateStatus(self, newStatus):
		self.status = newStatus




Post.create_post({
	'message': 'hello world! 12',
	'author_id': 76,
	'status': 2,
	'timestamp': '35/1/10/2016'
})