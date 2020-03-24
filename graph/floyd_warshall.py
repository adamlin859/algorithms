"""

Input: a directed weighted graph G=(V, E, w) with real edge weights
Output: an n x n matrix D such that 
	
	D[i,j] = length of shortest path from i to j

Run Bellman ford once for every vertex O(n^2 m)
"""

def floyd_warshall(n, D):
	print(D)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				D[i][j] = min(D[i][j], D[i][k] + D[k][j])
	
	print(D)


if __name__ == "__main__":
	adj_table = [[0, 4, 5, float("inf")],
				 [float("inf"), 0, -1, 1],
				 [float("inf"), 2, 0 , -1],
				 [float("inf"), float("inf"), float("inf"), 0]]
	n = 4

	floyd_warshall(n, adj_table)