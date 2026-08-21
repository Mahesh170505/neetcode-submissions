class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sort = sorted(piles)
        left = 1
        right = sort[len(sort) - 1]
        ans = math.inf
        while(left <= right):
            mid = (left + right) // 2
            hours = 0
            for num in sort:
                val = -(-num // mid)
                hours += val
            if(hours <= h):
                right = mid - 1
                ans = min(ans, mid)
            else:
                left = mid + 1
        return ans