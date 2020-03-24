
def kruskals(V, E):
	E_t = set()
	edges = [(v, k) for k,v in] 
	edges.sort()

	trees = set()
	for u in V:
		trees.add(set(u))

	

	for i, edge in edges:
		u = edge[0]
		v = edge[1]

		u_set = find(u, trees)
		v_set = find(v, trees)

		if u_set != v_set:
			E_t.add(edge)
			trees -= u_set
			trees -= v_set
			trees.add(u_set.union(v_set))


def find(u, trees):
	for tree in trees:
		if u in tree:
			return tree



