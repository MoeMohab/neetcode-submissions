class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def equation(n1, n2, op):
            if op == '+':
                return n1 + n2
            elif op == '-':
                return n1 - n2
            elif op == '*':
                return n1 * n2
            else:
                return n1 / n2
        
        op = set(['+', '-', '*', '/'])

        s = []

        for i in tokens:
            if i in op:
                n2 = s.pop()
                n1 = s.pop()
                s.append(int(equation(n1, n2, i)))
            else:
                s.append(int(i))
        
        return s[-1]