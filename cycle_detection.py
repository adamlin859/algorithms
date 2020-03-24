
class detect_odd_cycle:
	def __init__(self, V, E):
		self.V = V
		self.E = E
		self.time = 0
		self.start = {}
		self.finish = {}

	def find(self):
		self.explore = {}
		for u in self.V:
			self.explore[u] = 0

		for u in self.V:
			if self.explore[u] == 0:
				self.search(u)

	def search(self, u):
		self.previsit(u)
		self.explore[u] = 1

		for v in E[u]:
			if self.explore[v] == 0 
				self.search(u)
			else:
				length = self.start[v] - self.end[v]
				if length % 2 != 0 
					return True
		self.postvisit(u)

	def previsit(self, u):
		self.time += 1
		self.start[u] = time 

	def postvisit(self, u):
		self.time += 1 
		self.finish[u] = time