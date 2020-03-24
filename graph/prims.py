
def prim(V, E, w, s):
	for v in V:
		dist[v] = float("inf")
		prev[v] = None

	dist[s] = 0 
	
	Q = heapify([(v, k) for k, v in dist.items()])
	S = set()

	while len(Q) != 0:
		u = heappop(Q)
		S.add(u)

		for v in E[u]:
			if v in V - S:
				if dist[v] > w[(u, v)]:
					dist[v] = w[(u, v)]
					prev[v] = u 

					# decrease key
					# need to check this						

