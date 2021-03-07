class Book:

	def __init__(self, name, read):
		self.name = name
		self.read = read

	def set_read(self):
		if self.read:
			self.read = 0
		else:
			self.read = 1
