class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            curr = operations[i]
            if(curr == "+"):
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif(curr == "D"):
                stack.append(int(stack[-1]) * 2)
            elif(curr == "C"):
                stack.pop()
            else:
                stack.append(int(curr))
        
        Sum = 0
        for i in range(len(stack)):
            curr = stack[i]
            Sum += curr
        return Sum
