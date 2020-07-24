from collections import deque

class Node:
    """ data structure represent a vertex in the graph"""
    def __init__(self):
        self.nextCourses = []
        self.inDegrees = 0

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        relation_dict = {}
        total_edges = 0
        
        for edge in prerequisites:
            inbound, outbound = edge[0], edge[1]
            total_edges += 1
            if outbound not in relation_dict:
                relation_dict[outbound] = Node()
            relation_dict[outbound].nextCourses.append(inbound)
            
            if inbound not in relation_dict:
                relation_dict[inbound] = Node()
            relation_dict[inbound].inDegrees += 1
        
        # Topological search
        bfs_queue = deque()
        # first append all nodes with no inbound degrees
        for index, node in relation_dict.items():
            if node.inDegrees == 0:
                bfs_queue.append(index)
        
        removed_edges = 0
        while bfs_queue:
            # pop out course without dependency
            curr_node = bfs_queue.popleft()
            
            for next_course in relation_dict[curr_node].nextCourses:
                removed_edges += 1
                relation_dict[next_course].inDegrees -= 1
                
                if relation_dict[next_course].inDegrees == 0:
                    bfs_queue.append(next_course)
        
        return total_edges == removed_edges
