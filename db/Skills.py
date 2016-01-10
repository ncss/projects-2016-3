class Skills:
	def __init__ (self, category, rank, spec):
		self.category = category
		self.rank = rank
		self.spec = spec

	def __str__(self):
		return 'Obect for user\'s skills {}'.format(self.skills)
