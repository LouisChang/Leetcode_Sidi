class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        current_location = 0
        locator1, locator2 = [], []
        for word in words:
            if word == word1:
                locator1.append(current_location)
            if word == word2:
                locator2.append(current_location)
            current_location += 1
            
        shortest_distance = len(words)
        i = j = 0
        while i < len(locator1) and j < len(locator2):
            curr_distance = abs(locator1[i] - locator2[j])
            if curr_distance < shortest_distance:
                shortest_distance = curr_distance
            if locator1[i] < locator2[j]:
                i += 1
            else:
                j += 1
        
        return shortest_distance
        