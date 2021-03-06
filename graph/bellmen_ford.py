"""
OPT(i, v) cost of a shortest s-v path with at most i edges 

If the path uses at most i-1 edges then 
    
    OPT(i, v) = OPT(i-1, v)

if the path uses i edges
    
    OPT(i, v) = min {OPT(i-1, x) + w(x, v)}

Running time O(mn)
"""


def bellmen_ford(V, E, w, s):

    n = len(V)
    dp = {}

    # edge cases
    for v in V:
        dp[(0, v)] = float("inf")

    dp[(0, s)] = 0

    for i in range(1, n):
        # detection negative cycle and stoping 
        no_change = True 

        for v in V:
            min_dist = dp[i - 1, v]
            for x in V:
                if v in E[x]:

                    dist = dp[i - 1, x] + w[(x, v)]
                    if min_dist > dist:
                        no_change = False
                        min_dist = dist
            dp[i, v] = min_dist

        
        
        if no_change:
            break


    print(dp)

if __name__ == "__main__":

    V = {"S","a","b", "c"}
    E = {"S":["a", "b"], "a":["c", "b"],"b":["a","c"], "c":[]}
    w = {("S","a"):4, ("a","c"):1, ("S","b"):5, ("b","c"):-1, ("a","b"):-1,("b","a"):2}

    bellmen_ford(V, E, w, "S")