class DirectedGraph():
	def __init__(self, vertices):
		self.adjacents = {}
		self.V = vertices

	def insert(self, key, value):
		if key in self.adjacents:
			if self.adjacents[key] and value is not None:
				self.adjacents[key].append(value)
			return
	
		if value is None:
			self.adjacents[key] = []
		else:
			self.adjacents[key] = [value]

	def get(self):
		return self.adjacents


	def topological_sort_util(self, key, visited, stack):
		visited[key] = True

		if key in self.adjacents: 		
			for i in self.adjacents[key]:
				if visited[i] == False:
					self.topological_sort_util(i, visited, stack)

		stack.insert(0, key)


	def topological_sort(self):
		visited = [False] * self.V
		stack = []

		for i in range(self.V):
			if visited[i] == False:
				self.topological_sort_util(i, visited, stack)

		return stack


