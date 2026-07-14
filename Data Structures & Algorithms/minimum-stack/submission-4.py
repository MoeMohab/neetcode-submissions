class Node:
    def __init__(self, val, min):
        self.val = val
        self.min = min
    
class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append(Node(val, val))
        else:
            minim = self.getMin()
            self.s.append(Node(val, min(minim, val)))

    def pop(self) -> None:
        if self.s:
            self.s.pop()

    def top(self) -> int:
        if not self.s:
            return 0
        return self.s[-1].val

    def getMin(self) -> int:
        if not self.s:
            return 0
        return self.s[-1].min
        
