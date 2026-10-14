class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # contain indices
        l = r = 0 # where slider starts

        while r < len(nums):
            # make sure no smaller values exist in deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window if out of bounds
            if l > q[0]:
                q.popleft()

            # edge case: check that window is at least size k

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1 # only incremented when window is size k
            r += 1

        return output
