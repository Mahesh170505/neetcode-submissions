class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = sorted(list(zip(position, speed)), reverse = True)
        stack = []
        for i in range(len(result)):
            tta = (target - result[i][0]) / result[i][1]
            if(stack and tta in stack):
                continue
            elif (stack and tta <= stack[-1]):
                continue
            else:
                stack.append(tta)
        return len(stack)