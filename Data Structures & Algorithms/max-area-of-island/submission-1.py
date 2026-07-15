from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def get_neighbors(coords):
            r,c = coords
            dRows = [-1, 0, 1, 0]
            dCols = [0, -1, 0, 1]
            res = []
            for i in range(len(dRows)):
                nr = r + dRows[i]
                nc = c + dCols[i]
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 0:
                    res.append((nr, nc))
            return res

        def bfs(r, c):
            q = deque([(r, c)])
            visited = set([(r, c)])
            size = 0
            while q:
                coords = q.popleft()
                size += 1
                for neighs in get_neighbors(coords):
                    if neighs in visited:
                        continue
                    q.append(neighs)
                    visited.add(neighs)
                grid[coords[0]][coords[1]] = 0
            return size

        n, m = len(grid), len(grid[0])
        mSize = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    mSize = max(mSize, bfs(i, j))

        return mSize


