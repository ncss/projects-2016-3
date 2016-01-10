class User:
	def __init__ (self, user_id, email, fname, lname, DOB, location, gender, photo, phone):
		self._user_id = user_id
		self._email = email
		self._fname = fname
		self._lname = lname
		self._DOB = DOB
		self._location = location
		self._gender = gender
		self._photo = photo
		self._phone = phone

	def __str__(self):
		return 'Obect for user {}'.format(self.name)

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

#********************************************************************************
#********************************************************************************
#Sign in and log in
#********************************************************************************
#********************************************************************************

	def email_exists(email):
		#TODO
		pass
		if select(<email>):
			return True
		else:
			return False	

	@classmethod
	def create_user(email, fname, lname, DOB, location, gender, password):
		#TODO
		pass
		newUser = insert(<fields>):
			return newUser
		else:
			return None	

	def get_person(user_id):
		#TODO
		pass
		return select(<user_id>)
	
	def get_person(email):
		#TODO
		pass
		return select(<email>)

	def verify_password(email, password):
		#TODO
		pass
		if email == select(<email>):
			if password == select(<password>):
				return True
			else:
				return False #Incorrect password
		else:
			return False #Incorrect email


#********************************************************************************
#********************************************************************************
#Fun stuff
#********************************************************************************
#********************************************************************************

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

