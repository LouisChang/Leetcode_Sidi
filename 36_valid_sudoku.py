class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # get the line, row is a list of str
        for row in board:
            dicr = {}
            for num in row:
                if num == '.':
                    continue
                if num in dicr:
                    return False
                else:
                    dicr[num] = 1
        # check each column
        for col in range(len(board)):
            dicc = {}
            for num in range(len(board[col])):
                if board[num][col] == '.':
                    continue
                if board[num][col] in dicc:
                    return False
                else:
                    dicc[board[num][col]] = 1
        
        # Check each small square
        for i in range(3):
            for j in range(3):
                dics = {}
                for row in range(3*i,3*i+3):
                    for col in range(3*j,3*j+3):
                        if board[row][col] == '.':
                            continue
                        if board[row][col] in dics:
                            
                            return False
                        else:
                            dics[board[row][col]] = 1
                            print(dics[board[row][col]])
        
        
        return True
