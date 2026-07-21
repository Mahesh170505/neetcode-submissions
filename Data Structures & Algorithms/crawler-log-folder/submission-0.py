class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for i in range(len(logs)):
            log = logs[i]
            if(depth == 0 and log == "../"):
                depth = 0
            elif(log == "./"):
                continue
            elif(depth != 0 and log == "../"):
                depth -= 1
            else:
                depth +=1
        return depth