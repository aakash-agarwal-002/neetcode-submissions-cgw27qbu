class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [0]*n
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        print(graph)
        
        def dfs(i):
            visited[i] = 1
            for j in graph[i]:
                if visited[j]==0:
                    dfs(j)
        res = 0
        for i in range(n):
            if visited[i]==0:
                print(i)
                res+=1
                dfs(i)
        return res