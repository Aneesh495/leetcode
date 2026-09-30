from bisect import bisect_right

class Solution:
    def kthRemainingInteger(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        prefix_even = [0]
        for value in nums:
            prefix_even.append(prefix_even[-1] + (value % 2 == 0))

        answer = []
        for left_index, right_index, k in queries:
            low, high = k, k + (right_index - left_index + 1)
            while low < high:
                middle = (low + high) // 2
                end = bisect_right(nums, 2 * middle, left_index, right_index + 1)
                removed = prefix_even[end] - prefix_even[left_index]
                if middle - removed >= k:
                    high = middle
                else:
                    low = middle + 1
            answer.append(2 * low)
        return answer