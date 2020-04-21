class graph:
	def __init__(self, graph, heuristics):
		self.graph = graph
		self.heuristics = heuristics

	def get_neighbours(self, node):
		return self.graph[node]

	def get_heuristic(self, node):
		return self.heuristics[node]

	def get_a_star_score(self, node, g): # g = g(n)
		# will return cost of path to [start_node] + heuristic of node
		return self.get_heuristic(node) + g
	
	def a_star_algorithm(self, start_node, stop_node):
		open_list = [start_node] # nodes evaluated but not expanded on
		closed_list = [] # nodes expanded on

		g = {} # will contain g(n), distance from start_node, for all nodes
		g[start_node] = 0

		parents = {} # will be used to keep paths
		parents[start_node] = start_node

		found = False

		while open_list:
			curr_node = None
			for node in sorted(open_list):
				# selecting node with lowest A* score (g(n) + h(n))
				if curr_node == None:
					curr_node = node
				else:
					scoreA = self.get_a_star_score(curr_node, g[curr_node])
					scoreB = self.get_a_star_score(node, g[node])
					if scoreB < scoreA:
						curr_node = node

			if curr_node == stop_node:
				found = True
				print("Path Found")
				
				path = []
				path.append(curr_node)
				node = curr_node
				while node != start_node:
					node = parents[node]
					path.append(node)
				path.reverse()
				print("-> " + str(path))
				print("-> Cost: " + str(g[stop_node]))
				break
			
			else:
				open_list.remove(curr_node)
				closed_list.append(curr_node)
				for (neighbour, weight) in self.get_neighbours(curr_node):
					if neighbour in closed_list:
						continue # will skip the current iteration
					elif neighbour in open_list:
						# if specific node is already in open_list we can compare its g(n) value and the new g(n)
						# if new g(n) value is lower than old then we will update the values of g[n] and parent[n]
						new_g = g[curr_node] + weight
						if new_g > g[neighbour]:
							continue # will skip current iteration as new value is greater

					g[neighbour] = g[curr_node] + weight
					parents[neighbour] = curr_node
						
					if neighbour not in open_list and neighbour not in closed_list:
						open_list.append(neighbour)
		if found == False:
			print("No Path Found")

if __name__ == "__main__":
	g = {
		"S": [("B", 4), ("C", 3)],
		"B": [("E", 12), ("F", 5)],
		"C": [("D", 7), ("E", 10)],
		"D": [("E", 2)],
		"E": [("G", 5)],
		"F": [("G", 16)],
		"G": []
	}

	h = {
		"S": 14,
		"B": 12,
		"C": 11,
		"D": 6,
		"E": 4,
		"F": 11,
		"G": 0
	}

	a_star = graph(g, h)

	a_star.a_star_algorithm("S", "G")
