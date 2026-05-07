class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cond_one =  True if len(edges)==n-1 else False # num of edges = n-1
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


        for i in range(n):
            if visited[i]==0:
                dfs(i)
                if sum(visited)<n:
                    return False
        return cond_one