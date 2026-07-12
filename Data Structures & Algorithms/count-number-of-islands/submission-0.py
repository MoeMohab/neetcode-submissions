class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_neighbors(r, c):
            deltaR = [-1, 0, 1, 0]
            deltaC = [0, -1, 0, 1]
            res = []
            for i in range(len(deltaR)):
                nr = r + deltaR[i]
                nc = c + deltaC[i]
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "0":
                    res.append((nr, nc))
            return res

        def dfs(r, c, visited):

            visited.add((r, c))
            for nr, nc in get_neighbors(r, c):
                if (nr, nc) in visited:
                    continue
                grid[nr][nc] = "0"
                dfs(nr, nc, visited)
            
        n,m = len(grid), len(grid[0])
        count  = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j, set([(i, j)]))
        return count