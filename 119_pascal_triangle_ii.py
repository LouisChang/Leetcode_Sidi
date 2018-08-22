class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for r in range(1,rowIndex+1):
            col = r
            curr_row = [1] * (col+1)
            for c in range(1, len(curr_row)-1):
                curr_row[c] = res[c-1] + res[c]
            res = curr_row
        return res
