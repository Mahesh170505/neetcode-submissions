class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = sorted(piles)
        left = 1
        right = result[len(result) - 1]
        ans = math.inf
        while(left <= right):
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans