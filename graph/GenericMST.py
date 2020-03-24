"""
A minimum spanning tree (MST) or minimum weight spanning tree is 
a subset of the edges of a connected, edge-weighted undirected graph 
that connects all the vertices together, without any cycles and with 
the minimum possible total edge weight. 

"""
def generic_MST(V, E, w):
	E_t = set()
	n = len(V)
	while len(E_t) <= n - 1:
		 