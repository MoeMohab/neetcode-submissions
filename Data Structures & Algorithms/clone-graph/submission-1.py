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
        def dfs(node):
            if node in mapped:
                return mapped[node]
            copy = Node(node.val)
            mapped[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        if not node:
            return None
        mapped = {}
        
        return dfs(node) if node else None
