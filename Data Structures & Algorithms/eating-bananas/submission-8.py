class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = sorted(piles)
        low = 1
        high = result[len(result) - 1]
        ans = math.inf
        while low <= high:
            mid = (low + high) // 2
            hours = 0 
            for i in result:
                hours += math.ceil(i / mid)
            if hours <= h:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans
