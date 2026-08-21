class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = sorted(piles)
        left = 1
        right = result[len(result) - 1]
        speed = math.inf
        while(left <= right):
            hours = 0
            mid = (left + right) // 2
            for i in range(len(result)):
                hours += -(-result[i] // mid)
            if(hours <= h):
                right = mid - 1
                speed = min(speed, mid)
            else:
                left = mid + 1
        return speed