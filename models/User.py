from . import dbfunctions as db
from . import Skill


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

    # Everything after this point needs to be updated in the database too!

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

    def get_skills(self):
        skills = db.select('skills s inner join user_skills us', 'us.user_id = %d' % (self._user_id), 's.skill_id', 's.category', 's.specialisation', 's.rank')
        return [Skill.Skill(s[0], s[1], s[3], s[2]) for s in skills]

    def set_skills(self, skills):
        db.delete('user_skills', 'user_id = %d' % self._user_id)
        for skill in skills:
            skill_id = db.select('skills', 'specialisation = \'%s\'' % skill, 'skill_id')
            if skill_id:
                db.insert('user_skill', {
                    'skill_id': skill_id,
                    'user_id': self._user_id
                })


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
        person_list = db.select('user', whereClause, 'user_id', 'email', 'fname', 'lname', 'DOB', 'location', 'gender', 'photo', 'phone', 'password')
        print('PERSON', person_list)
        #make above line into a dictionary
        person_list, = person_list
        new_user = User(person_list[0], person_list[1], person_list[2],
                person_list[3], person_list[4], person_list[5],
                person_list[6], person_list[7], person_list[8],
                person_list[9])
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

    @classmethod
    def updatePhoto(cls, user_id, newPhoto):
        db.update('user', 'photo', newPhoto, 'user_id = {}'.format(user_id))

    @classmethod
    def updateContact(cls, user_id, newContact):
        db.update('user', 'email', newContact, 'user_id = {}'.format(user_id))
