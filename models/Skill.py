from . import dbfunctions as db

class Skill:
    def __init__ (self, skill_id, category, rank, spec):
        self._skill_id = skill_id
        self._category = category  # str
        self._rank = rank  # int
        self._spec = spec  # int

    def __str__(self):
        return 'Object for skill: category {}, rank {}, specialisation {}'.format(self.category, self.rank, self.spec)

    def get_skill_id(self):
        return self._skill_id

    def get_category_id(self):
        return self._category

    def get_rank(self):
        return self._rank

    def get_spec(self):
        return self._spec

    @classmethod
    def create_skill(cls, column_values):
        inserted_id = db.insert('skills', column_values)
        new_skill = Skill(inserted_id, column_values.get('category'), column_values.get('rank'), column_values.get('spec'))
        return new_skill

    @classmethod
    def get_all_skills(cls):
        skill_list = []
        skill_data = db.select('skills', None, 'skill_id', 'category', 'specialisation', 'rank')
        for line in skill_data:
            new_skill = Skill(line[0], line[1], line[2], line[3])
            skill_list.append(new_skill)
        return skill_list

    @classmethod
    def get_skill_by_id(cls, skill_id):
        where_clause = 'skill_id = {}'.format(skill_id)
        skill_dict = db.select('skills', where_clause, 'skill_id', 'category', 'specialisation', 'rank')
        new_skill = Skill(skill_dict.get('skill_id'), skill_dict.get('category'), skill_dict.get('specialisation'), skill_dict.get('rank'))
        return new_skill

if __name__ == '__main__':
    print(str(Skill(0, 1, 2)))
