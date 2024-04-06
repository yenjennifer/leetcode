class Solution:
    def isValidSudoku(self, board) -> bool:

        #box#
        k = 0
        while k<=6:
            l=0
            while l<=6:
                seen = set()
                for i in range(0+k,3+k):
                    for j in range(0+l,3+l):
                        if board[i][j] == ".": continue
                        if board[i][j] in seen: return False
                        seen.add(board[i][j])
                l+=3
            k+=3
            
        for i in range(9):
            #row#
            seen = set()
            for val in board[i]:
                if val == ".": continue
                if val in seen: return False
                seen.add(val)
            #column#
            seen = set()
            for j in range(9):
                if board[j][i] == ".": continue
                if board[j][i] in seen: return False
                seen.add(board[j][i])
        return True

if __name__ == '__main__':
    s = Solution()
    board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    print(s.isValidSudoku(board))

