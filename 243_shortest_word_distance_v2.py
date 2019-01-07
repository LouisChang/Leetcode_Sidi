class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        current_location = 0
        locator1, locator2 = -1, -1
        shortest_distance = len(words)
        for word in words:
            if word == word1:
                locator1 = current_location
            if word == word2:
                locator2 = current_location
            
            if locator1 != -1 and locator2 != -1:
                shortest_distance = min(shortest_distance, abs(locator1-locator2))
            current_location += 1
            
        return shortest_distance
            
        
