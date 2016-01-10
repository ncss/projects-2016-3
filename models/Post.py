class Post:
	def __init__ (self, title, message, author, status):
		self.title = title
		self.message = message
		self.author = author
		self.status = status

	def __str__(self):
		return 'Obect for post {} by {}'.format(self.title, self.author)

	'''
	Everything after this point needs to be updated in the database too!
	'''

	#def newPost(self, title, message, author, status):
	#def Post(self, title, message, author, status):

	def updateTitle(self, newTitle):
		self.title = newTitle
	
	def updateMessage(self, newMessage):
		self.message = newMessage

	def updateStatus(self, newStatus):
		self.status = newStatus