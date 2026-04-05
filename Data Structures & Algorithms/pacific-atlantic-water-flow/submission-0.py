from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        
        pacific_visited = [[False] * n for _ in range(m)]
        atlantic_visited = [[False] * n for _ in range(m)]
        
        pacific = deque()
        atlantic = deque()
        
        # Add Pacific border cells
        for i in range(m):
            pacific.append((i, 0))
            pacific_visited[i][0] = True
        for j in range(n):
            pacific.append((0, j))
            pacific_visited[0][j] = True
        
        # Add Atlantic border cells
        for i in range(m):
            atlantic.append((i, n - 1))
            atlantic_visited[i][n - 1] = True
        for j in range(n):
            atlantic.append((m - 1, j))
            atlantic_visited[m - 1][j] = True
        
        def bfs(queue, visited):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        not visited[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        visited[nr][nc] = True
                        queue.append((nr, nc))
        
        bfs(pacific, pacific_visited)
        bfs(atlantic, atlantic_visited)
        
        result = []
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    result.append([i, j])
        
        return result
