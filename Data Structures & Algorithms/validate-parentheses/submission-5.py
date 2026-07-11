class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if(i == '('):
                stack.append('(')
            elif(i == '{'):
                stack.append('{')
            elif(i == '['):
                stack.append('[')
            else:
                if(i == ')' and stack and stack[-1] == '('):
                    stack.pop()
                elif(i == '}' and stack and stack[-1] == '{'):
                    stack.pop()
                elif(i == ']' and stack and stack[-1] == '['):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0