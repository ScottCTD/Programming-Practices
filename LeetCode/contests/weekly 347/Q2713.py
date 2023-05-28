from typing import List


# TODO
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        # construct the graph:
        # v -> u if and only if v and u are on the same row or column, and u > v
        # we find the maximum length of paths in that graph
        m, n = len(mat), len(mat[0])
        graph = {}
        for i in range(m):
            for j in range(n):
                e = mat[i][j]
                children = []
                for k in range(m):
                    if mat[k][j] > e:
                        children.append((k, j))
                for k in range(n):
                    if mat[i][k] > e:
                        children.append((i, k))
                graph[(i, j)] = children
        answer = 0
        for node in graph:
            queue = [node]
            depth = 0
            while queue:
                new_queue = []
                for v in queue:
                    new_queue.extend(graph[v])
                queue = new_queue
                depth += 1
            answer = max(answer, depth)
        return answer


s = Solution()
print(s.maxIncreasingCells([[3, 1], [3, 4]]))
print(s.maxIncreasingCells([[1, 1], [1, 1]]))
print(s.maxIncreasingCells([[3, 1, 6], [-9, 5, 7]]))
import random
size = random.randint(1, 10 ** 5 // 2)
print(s.maxIncreasingCells([[random.randint(1, 10 ** 5) for _ in range(size)] for _ in range(size)]))
