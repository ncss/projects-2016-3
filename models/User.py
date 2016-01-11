import dbfunctions as db

class User:
	def __init__ (self, user_id, email, fname, lname, DOB, location, gender, photo, phone, password):
		self._user_id = user_id
		self._email = email
		self._fname = fname
		self._lname = lname
		self._DOB = DOB
		self._location = location
		self._gender = gender
		self._photo = photo
		self._phone = phone
		self._password = password

	def __str__(self):
		return 'Object for user {}'.format(self.name)

	'''
	Everything after this point needs to be updated in the database too!
	'''
#********************************************************************************
#********************************************************************************
#Return fields
#********************************************************************************
#********************************************************************************
	def get_user_id(self):
		return self._user_id

	def get_email(self):
		return self._email

	def get_first_name(self):
		return self._fname

	def get_last_name(self):
		return self._lname

	def get_DOB(self):
		return self._DOB

	def get_age(self):
		#Calulate age from DOB
		return self._DOB

	def get_location(self):
		#Split into long/lat
		return self._location

	def get_gender(self):
		return self._gender

	def get_photo(self):
		#Ask Bruce
		return self._photo

	def get_phone(self):
		return self._phone

	def get_password(self):
		return self._password
#********************************************************************************
#********************************************************************************
#Sign in and log in
#********************************************************************************
#********************************************************************************
	
	@classmethod
	def email_exists(klass, email):
		#To check
		if select(email, 'user'):
			return True
		else:
			return False	

	@classmethod
	def create_user(klass, email, fname, lname, DOB, location, gender, password):
		#TODO
		pass
		'''
		newUser = insert(<fields>):
			return newUser
		else:
			return None	
		'''
	@classmethod
	def get_person(klass, user_id):	
		return select('user','user_id = %s' % user_id, 'user_id', 'fname', 'lname', 'DOB', 'location', 'gender', 'phone', 'password')
		
		#return select(user_id, user)
		
	@classmethod
	def get_person(klass, email):
		#TODO
		email = "email = " + email
		return select('user', email, 'user_id', 'fname', 'lname', 'DOB', 'location', 'gender', 'phone')
		

	@classmethod
	def verify_password(klass, email, password):
		#TODO
		pass
		'''	
		if email == select(<email>):
			if password == select(<password>):
				return True
			else:
				return False #Incorrect password
		else:
			return False #Incorrect email
		'''

#********************************************************************************
#********************************************************************************
#Fun stuff
#********************************************************************************
#********************************************************************************
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
'''
