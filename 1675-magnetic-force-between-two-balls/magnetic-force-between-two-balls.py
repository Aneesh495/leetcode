class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        lo,hi = 1, (position[-1]-position[0])//(m-1)
        while lo < hi:
            mid = (lo+hi+1)//2
            count, last = 1, position[0]
            for x in position[1:]:
                if x-last >= mid:
                    count += 1; last = x
            if count >= m: lo = mid
            else: hi = mid-1
        return lo