class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # edge cases
        if numRows == 0:
            return []
        res = [[1]]
        for row in range(1,numRows):
            curr_row = [1]*(row+1)
            for col in range(1,len(curr_row)-1):
                curr_row[col] = res[row-1][col] + res[row-1][col-1]
            res.append(curr_row)
        return res
