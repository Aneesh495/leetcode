
from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(cur: int, forward: bool) -> int:
            # invalid if direction changes or element zeroed
            if nums[cur] == 0 or (nums[cur] > 0) != forward:
                return -1
            nxt = (cur + nums[cur]) % n
            # invalid if self loop of length one
            if nxt == cur:
                return -1
            return nxt

        for i in range(n):
            if nums[i] == 0:
                continue
            forward = nums[i] > 0
            slow = i
            fast = i
            # Floyd cycle detection with direction guard
            while True:
                slow = next_index(slow, forward)
                if slow == -1:
                    break
                fast = next_index(fast, forward)
                if fast == -1:
                    break
                fast = next_index(fast, forward)
                if fast == -1:
                    break
                if slow == fast:
                    return True
            # cleanup visited nodes from i along the same direction
            j = i
            sign = 1 if forward else -1
            while nums[j] * sign > 0:
                nxt = (j + nums[j]) % n
                nums[j] = 0
                if nxt == j:
                    break
                j = nxt
        return False
