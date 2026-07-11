class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            stack = [node]
            visited[node] = True
            vertices = 0
            edge_count = 0

            while stack:
                curr = stack.pop()
                vertices += 1
                edge_count += len(graph[curr])

                for nei in graph[curr]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

            return vertices, edge_count // 2

        complete = 0

        for i in range(n):
            if not visited[i]:
                vertices, edges_in_component = dfs(i)
                if edges_in_component == vertices * (vertices - 1) // 2:
                    complete += 1

        return complete