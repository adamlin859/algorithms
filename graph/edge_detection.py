
class detect_odd_cycle:
	def __init__(self, V, E, e):
		self.V = V
		self.E = E
		self.time = 0
		self.e = e


	def find(self):
		self.explore = {}
		self.explore_edge = {}
		for u in self.V:
			self.explore[u] = 0
			for v in self.E[u]:
				self.explore_edge[(u, v)] = 0

		if (u, v) not in explore_edge:
			return False

		for u in self.V:
			if self.explore[u] == 0:
				self.search(u)
		return False

	def search(self, u):
		self.previsit(u)
		self.explore[u] = 1

		for v in self.E[u]:
			self.explore_edge[(u, v)] = 1
			if self.explore[v] == 0 
				self.search(u)
			else:
				if self.explore_edge[(u, v)] == 1:
					return True 

		self.postvisit(u)
