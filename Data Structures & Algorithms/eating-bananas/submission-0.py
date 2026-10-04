class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        result = r # at least this would work

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                result = min(result, k)
                r = k - 1 # get smaller rate
            else:
                l = k + 1 # get bigger rate

        return result