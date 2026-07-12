"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node, visited):
            if node not in mapped:
                mapped[node] = Node(node.val)
            for n in node.neighbors:
                if n in mapped:
                    mapped[node].neighbors.append(mapped[n])
                    continue
                mapped[n] = Node(n.val)
                mapped[node].neighbors.append(mapped[n])
                visited.add(n)
                dfs(n, visited)
                visited.remove(n)

        if not node:
            return None
        mapped = {}
        dfs(node, set())
        return mapped[node]
