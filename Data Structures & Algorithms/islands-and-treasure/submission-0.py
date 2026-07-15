INF = 2147483647
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def get_neighbors(coords):
            r,c = coords
            dRows = [-1, 0, 1, 0]
            dCols = [0, -1, 0, 1]
            res = []
            for i in range(len(dRows)):
                nr = r + dRows[i]
                nc = c + dCols[i]
                if 0 <= nr < n and 0 <= nc < m:
                    res.append((nr, nc))
            return res

        def bfs(r, c):
            q = deque([(r, c)])
            visited = set([(r, c)])
            level = 0
            while q:
                level += 1
                for _ in range(len(q)):
                    coords = q.popleft()
                    for neighs in get_neighbors(coords):
                        if neighs in visited or grid[neighs[0]][neighs[1]] in [-1, 0]:
                            continue
                        grid[neighs[0]][neighs[1]] = min(grid[neighs[0]][neighs[1]], level)
                        q.append(neighs)
                        visited.add(neighs)

        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    bfs(i, j)
