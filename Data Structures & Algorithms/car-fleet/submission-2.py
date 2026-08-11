class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = sorted(list(zip(position, speed)), reverse = True)
        ans = []
        for i in range(len(result)):
            time = (target - result[i][0]) / result[i][1]
            if ans and time in ans:
                continue
            elif ans and time < ans[-1]:
                continue
            else:
                ans.append(time)
        return len(ans)