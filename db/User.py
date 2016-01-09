class User:
	def __init__ (self, userID, email, fname, lname, age, location, gender, photo, contact):
		self.userID = userID
		self.email = email
		self.fname = fname
		self.lname = lname
		self.age = age
		self.location = location
		self.gender = gender
		self.photo = photo
		self.contact = contact

	def __str__(self):
		return 'Obect for user {}'.format(self.name)

	'''
	Everything after this point needs to be updated in the database too!
	'''

#Name Modifications
	def updateName(self, newName):
		self.name = newName

#Age Modifications	
	def updateAge(self, newAge):
		self.age = newAge

#Location Modifications
	def updateLocation(self, newLocation):
		self.location = newLocation

#Gender Modifications
	def updateGender(self, newGender):
		'''
		Store gender as:
			1. Boolean (i.e. True for male, False for female)
			2. Int (i.e. 0 for male, 1 for female)
			3. String (i.e. 'male'/'m' for male, 'female'/'f' for female)
		'''
		self.gender = newGender

#Skills Modifications
	def updateSkills(self, newSkills):
		self.skills = newSkills

	def appendSkill(self, newSkill):
		self.skills = self.skills.append(newSkill)

#Photo Modifications
	def updatePhoto(self, newPhoto):
		self.photo = newPhoto

#Contact Modifications
	def updateContact(self, newContact):
		self.contact = newContact

