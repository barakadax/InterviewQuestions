from collections import deque
from typing import List

class Solution: # BFS
    # Time: O(M * N) | Space: O(min(M, N))
    def numIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        islands_found = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    islands_found += 1
                    self._bfs_sink(grid, r, c, m, n)

        return islands_found

    # Time: O(M * N) | Space: O(min(M, N))
    def _bfs_sink(self, grid, r, c, m, n):
        queue = deque([(r, c)])
        grid[r][c] = 0

        while queue:
            row, col = queue.popleft()

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = row + dr, col + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    queue.append((nr, nc))


my_grid = [
    [1, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 0],
]

solver = Solution()
result = solver.numIslands(my_grid)
print(f"Number of islands: {result}")
