import User
import Skill

class UserSkill:
	def __init__(self, user_id, skill_id):
		self._user_id = user_id
		self._skill_id = skill_id

	def get_user_id(self):
		return self._user_id

	def get_skill_id(self):
		return self._skill_id

	def get_user_by_id(self):
		return User.get_person_by_id(self._user_id)

	def get_skill_by_id(self):
		return Skill.get_skill_by_id(self._skill_id)
