class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i].isdigit():
                stack.append(int(tokens[i]))

            elif tokens[i] == '+':
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)

            elif tokens[i] == '-':
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)

            elif tokens[i] == '*':
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)

            elif tokens[i] == '/':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))

            else:
                stack.append(int(tokens[i]))

        return stack.pop()