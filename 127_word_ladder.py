from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        # Pre-processing for dictionary list
        all_combined_keywords = {}
        
        # Assume all words share the same length
        L = len(beginWord)
        
        # Pre-add all word into dictionary, i.e., c*t: [cat]
        for word in wordList:
            for i in range(L):
                key = word[:i] + "*" + word[i+1:]
                if key not in all_combined_keywords:
                    all_combined_keywords[key] = [word]
                else:
                    all_combined_keywords[key].append(word)
                    
        # BFS to find shortest path
        keyword_queue = deque()
        visited = {}
        keyword_queue.append((beginWord,1))
        
        while len(keyword_queue) > 0 :
            word_tuple = keyword_queue.popleft()
            word, steps = word_tuple[0], word_tuple[1]
            visited[word] = True
            for i in range(L):
                key = word[:i] + "*" + word[i+1:]
                if key in all_combined_keywords:
                    for next_word in all_combined_keywords[key]:
                        if next_word not in visited:
                            if next_word == endWord:
                                return steps+1
                            keyword_queue.append((next_word, steps+1))
                            visited[next_word] = True
                        else:
                            pass
                        
        return 0
