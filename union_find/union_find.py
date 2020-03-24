

class union_find:
    def __init__(self):
        self.phi = {}
        self.rank = {}

    make_set(self, u):
        self.phi[u] = u # this store the parent of u 
        self.rank[u] = 0

    find(self, u):
        while self.phi[u] != u:
            u = self.phi[u]

        return u 

    union(self, u, v):
        r_u = self.find(u)
        r_v = self.find(v)

        if r_u == r_v:
            return 

        if self.rank[r_u] > self.rank[r_v]:
            self.rank[r_v] = r_u

        else:
            self.rank[r_u] = r_v

            if self.rank[r_u] == self.rank[r_v]:
                self.rank[r_v] = self.rank[r_v] + 1
            