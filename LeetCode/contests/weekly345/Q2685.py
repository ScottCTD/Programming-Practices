from typing import List

# 2023-05-14 00:51:55
# contest question
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # construct adjacency list
        graph = {}
        for edge in edges:
            a, b = edge
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int, component: List[int]):
            visited.add(node)
            component.append(node)
            for child in graph[node]:
                if child in visited:
                    continue
                dfs(child, component)

        visited = set()
        res = 0
        for root in graph.keys():
            if root not in visited:
                # get a component
                component = []
                dfs(root, component)
                # verify if it is a complete component
                # complete components have (n - 1)n / 2 edges
                edges = sum(len(graph[c]) for c in component) // 2
                m = len(component)
                if edges == (m - 1) * m // 2:
                    res += 1
        return res + n - len(visited)


s = Solution()
print(s.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))
