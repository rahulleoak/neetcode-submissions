class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        
    def find(self, vertex):
        if vertex not in self.parent:
            self.parent[vertex] = vertex
            self.rank[vertex] = 1
        
        root = vertex
        while root != self.parent[root]:
            self.parent[root] = self.parent[self.parent[root]]
            root = self.parent[root]
        
        return root

    def union(self, v1, v2):
        p1 , p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()

        emailToName = {}
        for account in accounts:
            name = account[0]
            firstEmail = account[1]
            for email in account[1:]:
                emailToName[email] = name
                dsu.union(firstEmail, email)
        
        rootToEmail = defaultdict(list)
        for email in emailToName:
            rootEmail = dsu.find(email)
            rootToEmail[rootEmail].append(email) 
        
        res = []
        for root in rootToEmail:
            name = emailToName[root]
            emails = rootToEmail[root]
            res.append([name] + sorted(emails) )
        
        return res

