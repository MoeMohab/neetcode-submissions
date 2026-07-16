class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def get_neighbors(r, c):
            deltaRow = [-1, 0, 1, 0]
            deltaCol = [0, -1, 0, 1]
            res = []

            for i in range(len(deltaRow)):
                dR = r + deltaRow[i]
                dC = c + deltaCol[i]
                if 0 <= dR < n and 0 <= dC < m:
                    res.append((dR, dC))
            return res
        

        def dfs(node, corresponding):
            corresponding.add(node)
            visited.add(node)
            r, c = node
            for nR, nC in get_neighbors(r, c):
                if (nR, nC) in corresponding or heights[nR][nC] < heights[r][c]:
                    continue
                dfs((nR, nC), corresponding)
        
        n, m = len(heights), len(heights[0])
        res = set()
        pacificBorders = set([(0, c) for c in range(m)] + [(r, 0) for r in range(n)])
        atlanticBorders = set([(n-1, c) for c in range(m)] + [(r, m-1) for r in range(n)])
        grid = [[0 for  _ in range(m)] for _ in range(n)]
        pacificAdditional = set()
        atlanticAdditional = set()
        visited = set()
        for i in pacificBorders:
            dfs(i, pacificAdditional)
        visited = set()
        for i in atlanticBorders:
            dfs(i, atlanticAdditional)

        return [list(r) for r in atlanticAdditional & pacificAdditional]