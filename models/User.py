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
        return 'Object for user {}, {}'.format(self._fname, self._lname)

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
        whereClause = 'email = \'{}\''.format(email)
        if db.select('user', whereClause, 'email'):
            return True
        else:
            return False


    @classmethod
    def create_user(klass, columnvaluedict):
        if User.email_exists(columnvaluedict.get('email')):
            return None
        new_id = db.insert('user', columnvaluedict)
        newUser = User(new_id, columnvaluedict.get('email'), columnvaluedict.get('fname'), columnvaluedict.get('lname'), columnvaluedict.get('DOB'), columnvaluedict.get('location'), columnvaluedict.get('gender'), columnvaluedict.get('photo'), columnvaluedict.get('phone'), columnvaluedict.get('password'))
        return newUser

    @classmethod
    def get_person_by_id(klass, user_id):
        whereClause = 'user_id = \'{}\''.format(user_id)
        person_list = db.select('user', whereClause, 'user_id', 'email', 'fname', 'lname', 'DOB', 'location', 'gender', 'photo', 'phone', 'password')[0]
        #make above line into a dictionary
        new_user = User(person_list[0], person_list[1], person_list[2], person_list[3], person_list[4], person_list[5], person_list[6], person_list[7], person_list[8], person_list[9])
        return new_user

    @classmethod
    def get_person_by_email(klass, email):
        whereClause = 'email = \'{}\''.format(email)
        person_list = db.select('user', whereClause, 'user_id', 'email', 'fname', 'lname', 'DOB', 'location', 'gender', 'photo', 'phone', 'password')[0]
        #make above line into a dictionary
        new_user = User(person_list[0], person_list[1], person_list[2], person_list[3], person_list[4], person_list[5], person_list[6], person_list[7], person_list[8], person_list[9])
        return new_user

    @classmethod
    def verify_password(klass, email, password):
        whereClause = 'email = \'{}\''.format(email)
        inDb = db.select('user', whereClause, 'password')
        if inDb:
            if password == inDb[0][0]:
                return True
            else:
                return False #Incorrect password
        else:
            return False #Incorrect email

    @classmethod
    def updateFName(cls, user_id, newName):
        whereClause = 'user_id = \'{}\''.format(user_id)
        db.update('user', 'fname', newName, whereClause)

    @classmethod
    def updateLName(cls, user_id, newName):
        whereClause = 'user_id = \'{}\''.format(user_id)
        db.update('user', 'lname', newName, whereClause)

    @classmethod
    def updateDOB(cls, user_id, newDOB):
        whereClause = 'user_id = \'{}\''.format(user_id)
        db.update('user', 'DOB', newDOB, whereClause)

    @classmethod
    def updateLocation(cls, user_id, newLocation):
        whereClause = 'user_id = \'{}\''.format(user_id)
        db.update('user', 'Location', newLocation, whereClause)

    @classmethod
    def updateGender(cls, user_id, newGender):
        whereClause = 'user_id = \'{}\''.format(user_id)
        db.update('user', 'Gender', newGender, whereClause)

    @classmethod
    def updateSkills(cls, user_id, newskill_id):
        whereClause = 'user_id = \'{}\''.format(user_id)
        db.update('user', 'user_skills', newskill_id, whereClause)

        #columnvaluedict = {'skill_id': newskill_id}
        #db.insert('user_skills', columnvaluedict)

    @classmethod
    def updatePhoto(cls, user_id, newPhoto):
        db.update('user', 'photo', newPhoto, 'user_id = {}'.format(user_id))

    @classmethod
    def updateContact(cls, user_id, newContact):
        db.update('user', 'email', newContact, 'user_id = {}'.format(user_id))



'''
    def appendSkill(self, newSkill):
        self.skills = self.skills.append(newSkill)

#Contact Modifications
    def updateContact(self, newContact):
        self.contact = newContact
'''

'''
myDictionary = {'email' : 'george.com', 'fname' : 'george', 'lname' : 'bob', 'DOB' : '1999-12-09', 'location' : '-4.999, 78.908', 'gender' : 'M', 'photo': '...', 'phone' : '04 5678 5786', 'password' : 'cat1'}
newUser = User.create_user(myDictionary)
print (newUser)

newUser = User.get_person_by_email('george.com')
print(newUser)
#print(User.verify_password('george.com', 'bob1'))
'''