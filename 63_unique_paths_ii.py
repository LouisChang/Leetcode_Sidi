class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        path = []
        for i in range(len(obstacleGrid)):
            path.append([0]*(len(obstacleGrid[0])))
        
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] != 1:
                path[0][i] = 1
            else:
                break
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] != 1:
                path[i][0]= 1
            else:
                break

        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1:
                    path[i][j] = path[i-1][j] + path[i][j-1]
                    
        return path[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
