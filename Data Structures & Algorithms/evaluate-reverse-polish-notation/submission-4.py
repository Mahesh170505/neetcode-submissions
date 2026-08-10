class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            elif(i == '+'):
                second = stack.pop()
                first = stack.pop()
                total = first + second
                stack.append(total)
            elif(i == '-'):
                second = stack.pop()
                first = stack.pop()
                total = first - second
                stack.append(total)
            elif(i == '*'):
                second = stack.pop()
                first = stack.pop()
                total = first * second
                stack.append(total)
            elif(i == '/'):
                second = stack.pop()
                first = stack.pop()
                total = int (first / second)
                stack.append(total)
        return stack[-1]
                