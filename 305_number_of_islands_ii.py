class DSU:
    def __init__(self):
        self.parents = {}
        self.rank = {}
        # self.size = {}
        self.count = 0
        
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            return
        else:
            self.count -= 1
            if self.rank[parent_x] < self.rank[parent_y]:
                parent_x, parent_y = parent_y, parent_x
            self.parents[parent_y] = parent_x
            
            if self.rank[parent_x] == self.rank[parent_y]:
                self.rank[parent_x] += 1
                
    
    def setParent(self, x):
        self.parents[x] = x
        self.rank[x] = 0
        # self.size[x] = 1
        self.count += 1

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        dsu = DSU()
        ans = []
        for po in positions:
            index = po[0]*n + po[1]
            dsu.setParent(index)
            for distance in [(0,1), (1,0), (0,-1),(-1,0)]:
                x, y = po[0] + distance[0], po[1] + distance[1]
                if 0 <= x < m and 0 <= y < n and x*n + y in dsu.parents:
                    dsu.union(index, x*n+y)
            ans.append(dsu.count)
            
        return ans