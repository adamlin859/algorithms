

def dijkstra_v1( V, E, w, s):
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
        # select a node  v \in V - S with at least one edge from S 
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


"""
Key idea: keep a conservative overestimate of the true length of the 
shortest s-v path in dist[v] as follows: when u is added to S 
update dist[v] for all v with (u, v) in E 

"""

def dijkstra_v2(V, E, w, s):
    # initaliztion 
    dist = {}
    prev = {}
    for v in V:
        dist[v] = float("inf")
        prev[v] = None
    dist[s] = 0
    
    S = set()

    while len(S) != len(V):
        nodes = V - S

        # pick u so that dist[u] is minimum among all nodes in V-S
        d_v = min([v for k, v in dist.items() if k in nodes])
        u = [key for key in nodes if dist[key] == d_v][0]

        S.add(u)

        for v in E[u]:
            # find a smaller edge to udate the original node
            if dist[v] > dist[u] +  w[(u, v)]:
                dist[v] = dist[u] + w[(u, v)]
                prev[v] = u 

    print(prev)
    print(dist)


"""
Key idea: using a priority queue implemented as a binary min-heap: store 
vertex u with key dist[u]. 

Running time O(n log n )

Need more time to think about
"""
# def dijkstra_v3(V, E, w, s):
#     # initaliztion 
#     dist = []
#     for v in V:
#         if v != s:
#             dist.append((float("inf"), v))
#         else:
#             dist.append((0, v))
#         prev[v] = None
    
#     heapify(x)
    
#     S = set()

#     while len(Q) != 0:
#         u = 

#         # pick u so that dist[u] is minimum among all nodes in V-S
#         d_v = min([v for k, v in dist.items() if k in nodes])
#         u = [key for key in nodes if dist[key] == d_v][0]

#         S.add(u)

#         for v in E[u]:
#             # find a smaller edge to udate the original node
#             if dist[v] > dist[u] +  w[(u, v)]:
#                 dist[v] = dist[u] + w[(u, v)]
#                 prev[v] = u 

#     print(prev)
#     print(dist)


if __name__ == "__main__":
    V = {"S","a","b", "c"}
    E = {"S":["a", "b"], "a":["c"],"b":["c"], "c":[]}
    w = {("S","a"):2, ("a","c"):1, ("S","b"):5, ("b","c"):1}


    dijkstra_v1( V, E,  w, "S")
    dijkstra_v2( V, E,  w, "S")




