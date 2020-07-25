from collections import deque

class Node:
    def __init__(self):
        self.nextCourses = []
        self.inDegrees = 0

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        graph = {}
        total_edges = 0

        non_prerequisites = [i for i in range(numCourses)]
        for course in non_prerequisites:
            graph[course] = Node()
        
        for courses in prerequisites:
            inbound, outbound = courses[0], courses[1]
            total_edges += 1
                
            graph[outbound].nextCourses.append(inbound)
            graph[inbound].inDegrees += 1
            
        bfs_queue = deque()
        res = []
        removed_edges = 0
        
        for index, node in graph.items():
            if node.inDegrees == 0:
                bfs_queue.append(index)
                
        while bfs_queue:
            curr_node = bfs_queue.popleft()
            res.append(curr_node)
            for next_course in graph[curr_node].nextCourses:
                graph[next_course].inDegrees -= 1
                removed_edges += 1
                
                if graph[next_course].inDegrees == 0:
                    bfs_queue.append(next_course)
                    
        if removed_edges == total_edges:
            return res
        else:
            return []
