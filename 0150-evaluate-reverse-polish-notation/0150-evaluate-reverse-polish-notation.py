import operator
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/":lambda a,b: int(a/b) if a*b >= 0 else - (abs(a) // abs(b))}

        stack = []
        for i in tokens:
            if i in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[i](a, b))
            else:
                stack.append(int(i))
        return stack[0]
        