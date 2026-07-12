from collections import defaultdict
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.refs = 0
        self.idx = -1
    
    def addWord(self, word, idx):
        node = self
        for char in word:
            node.refs += 1
            node = node.children[char]
        node.idx = idx

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def get_neighbors(node, trie, visited):
            row, col = node
            deltaRow = [-1, 0, 1, 0]
            deltaCol = [0, -1, 0, 1]
            ret = []
            for i in range(len(deltaRow)):
                nRow = row + deltaRow[i]
                nCol = col + deltaCol[i]
                if 0 <= nRow < n and 0 <= nCol < m and (nRow, nCol) not in visited and board[nRow][nCol] in trie.children:
                    ret.append((nRow, nCol))
            return ret

        def dfs(node, trie, visited):
            if trie.idx != -1:
                res.add(words[trie.idx])
                trie.refs -= 1
                # if trie.refs == 0:
                #     ch = board[node[0]][node[1]]
                #     trie.children[ch] = None

            for r,c in get_neighbors(node, trie, visited):
                visited.add((r, c))
                dfs((r, c), trie.children[board[r][c]], visited)
                visited.remove((r, c))
        
        t = Trie()
        n, m = len(board), len(board[0])
        for i in range(len(words)):
            t.addWord(words[i], i)
        res = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in t.children:
                    dfs((i, j), t.children[board[i][j]], set([(i, j)]))
        return list(res)











        



        