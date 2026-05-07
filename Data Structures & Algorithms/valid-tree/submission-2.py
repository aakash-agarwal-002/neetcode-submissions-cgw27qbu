class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
             return False
        graph = defaultdict(list)
        visited = [0]*n
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        def dfs(i):
            visited[i] = 1
            for j in graph[i]:
                if visited[j]==0:
                    dfs(j)
        dfs(0)
        return sum(visited)==n