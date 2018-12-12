class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        """
        : O(n^2) algorithm is not acceptale
        def maxFruit(subtree):
            count, total = 0, 0
            count_dic = {}
            for i in subtree:
                if i not in count_dic:
                    count_dic[i] = 1
                    count += 1
                    if count > 2:
                        break
                    else:
                        total += 1
                else:
                    total += 1
                    pass
            return total
        
        global_max = 0
        for start in range(len(tree)):
            global_max = max(global_max, maxFruit(tree[len(tree) - 1 - start:]))
            
        return global_max
        """
        """
        : Sliding the window, two pointers
        """
        ans = i = 0
        count = collections.Counter()
        # get each element into counter
        for j, x in enumerate(tree): # j is the index, x is the value
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        
        return ans
