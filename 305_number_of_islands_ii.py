class DSU:
    def __init__(self):
        self.parents = {}
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
            self.parents[parent_y] = parent_x
    
    def setParent(self, x):
        self.parents[x] = x
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
