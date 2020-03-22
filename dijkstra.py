

def dijkstra_v1( V, s, w):
    # initaliztion 
    dist = {}
    prev = {}
    for v in V:
        dist[v] = float("inf")
        prev[v] = None
    dist[s] = 0

    S = {s}
    while len(S) != len(V):
        nodes = V - S

        for v in nodes:
            min_dist = float("inf")
            min_node = None
            for u in S:
                if v in E[u]:
                    d_v = dist[u] + w[(u, v)]
                    if min_dist > d_v:
                        min_dist = d_v 
                        min_node = u

            if min_node:
                S.add(v)
                dist[v] = min_dist
                prev[v] = u

    print(prev)
    print(dist)


    



if __name__ == "__main__":
    V = {"S","a","b", "c"}
    E = {"S":["a", "b"], "a":["c"], "b":["c"]}
    w = {("S","a"):2, ("a","c"):1, ("S","b"):5, ("b","c"):1}


    dijkstra_v1( V, "S", w)




