class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def hasCycle(numNodes, edges):
            graph = defaultdict(list)
            indegree = [0] * numNodes

            # build graph
            for u, v in edges:
                graph[u].append(v)
                indegree[v] += 1

            # queue of nodes with indegree 0
            q = deque()
            for i in range(numNodes):
                if indegree[i] == 0:
                    q.append(i)

            count = 0

            while q:
                print(q)
                node = q.popleft()
                count += 1

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)

            return count == numNodes 

        
        return hasCycle(numCourses,prerequisites)