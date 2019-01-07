class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        current_location = 0
        appeared_word = []
        locator1, locator2 = -1, -1
        shortest_distance = len(words)
        if word1 == word2:
            flag = True
        else:
            flag = False
        for word in words:
            if flag:
                if word == word1:
                    appeared_word.append(current_location)
            else:
                if word == word1:
                    locator1 = current_location
                if word == word2:
                    locator2 = current_location

                if locator1 != -1 and locator2 != -1:
                    shortest_distance = min(shortest_distance, abs(locator1-locator2))
            current_location += 1
        
        if flag:
            if len(appeared_word) == 1:
                return 0
            for i in range(len(appeared_word)-1):
                shortest_distance = min(shortest_distance, appeared_word[i+1]-appeared_word[i])
            
        return shortest_distance
            
        
        
