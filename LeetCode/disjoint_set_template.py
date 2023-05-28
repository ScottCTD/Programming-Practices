from typing import List


class DisjointSet:
    n: int
    parents: List[int]
    rank: List[int]

    def __init__(self, n: int):
        """
        Initializes an int disjoint Set data structure (path compression + union by rank)
        of size n.
        :param n: size
        """
        self.n = n
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        """
        Finds with path compression.
        :param x: x < n
        :return: the representative of the tree that x belongs to
        """
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x: int, y: int) -> None:
        """
        Unions by rank.
        :param x: node x
        :param y: node y
        """
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]:
            self.parents[py] = px
        else:
            self.parents[px] = py
            if self.rank[px] == self.rank[py]:
                self.rank[py] += 1

    def is_connected(self, nodes: List[int]):
        """
        Checks if given nodes are connected.
        :param nodes: given list of nodes
                      Precondition: len(nodes) > 0
        :return: True if connected, or False otherwise
        """
        p = self.find(nodes[0])
        return all(self.find(nodes[i]) == p for i in range(1, len(nodes)))


def test_disjoint_set():
    ds = DisjointSet(5)
    assert ds.find(0) == 0
    assert ds.find(1) == 1
    assert ds.find(2) == 2
    assert ds.find(3) == 3
    assert ds.find(4) == 4

    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    assert ds.find(2) == 2
    assert ds.find(3) == 3
    assert ds.find(4) == 4

    ds.union(1, 2)
    assert ds.find(0) == ds.find(1) == ds.find(2)
    assert ds.find(3) == 3
    assert ds.find(4) == 4

    ds.union(3, 4)
    assert ds.find(0) == ds.find(1) == ds.find(2)
    assert ds.find(3) == ds.find(4)

    ds.union(2, 4)
    assert ds.find(0) == ds.find(1) == ds.find(2) == ds.find(3) == ds.find(4)

    ds.union(0, 4)
    assert ds.find(0) == ds.find(1) == ds.find(2) == ds.find(3) == ds.find(4)

    ds.union(1, 3)
    assert ds.find(0) == ds.find(1) == ds.find(2) == ds.find(3) == ds.find(4)
    assert ds.is_connected(list(range(5)))
    print('All test cases passed!')


if __name__ == "__main__":
    test_disjoint_set()
