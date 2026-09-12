class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = "+-*/"
        for i in tokens:
            if i not in op:
                stack.append(int(i))
            else:
                if i == "*":
                   stack.append(stack.pop() * stack.pop())
                elif i == "/":
                   r = stack.pop()
                   l = stack.pop()
                   stack.append(int(l / r))
                elif i == "+":
                   stack.append(stack.pop() + stack.pop())
                else:
                   r = stack.pop()
                   l = stack.pop()
                   stack.append(l - r)
        return stack[-1]
                

        