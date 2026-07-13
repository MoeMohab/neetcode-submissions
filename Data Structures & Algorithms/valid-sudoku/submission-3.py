from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j]) - 1
                if (1 << val) & rows[i]:
                    return False
                elif (1 << val) & cols[j]:
                    return False
                elif (1 << val) & squares[(i//3) * 3 + (j//3)]:
                    return False
                rows[i] |= (1 << val)
                cols[j] |= (1 << val)
                squares[(i//3) * 3 + (j//3)] |= (1 << val)
        return True
        # rows = defaultdict(set)
        # cols = defaultdict(set)
        # squares = defaultdict(set)

        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] == '.':
        #             continue
        #         elif (
        #             board[i][j] in rows[i]
        #             or board[i][j] in cols[j]
        #             or board[i][j] in squares[(i//3, j//3)] 
        #         ):
        #             return False
        #         rows[i].add(board[i][j])
        #         cols[j].add(board[i][j])
        #         squares[(i//3, j//3)].add(board[i][j])
        # return True