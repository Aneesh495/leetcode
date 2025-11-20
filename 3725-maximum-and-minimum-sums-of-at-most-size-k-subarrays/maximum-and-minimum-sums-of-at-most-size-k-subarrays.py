class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def counts_for_extreme(is_minimum: bool) -> list[int]:
            previous = [-1] * n
            stack = []
            for i, value in enumerate(nums):
                while stack and (nums[stack[-1]] >= value if is_minimum else nums[stack[-1]] <= value):
                    stack.pop()
                previous[i] = stack[-1] if stack else -1
                stack.append(i)

            following = [n] * n
            stack.clear()
            for i in range(n - 1, -1, -1):
                value = nums[i]
                while stack and (nums[stack[-1]] > value if is_minimum else nums[stack[-1]] < value):
                    stack.pop()
                following[i] = stack[-1] if stack else n
                stack.append(i)

            result = [0] * n
            limit_sum = k + 1
            for i in range(n):
                left_choices = i - previous[i]
                right_choices = following[i] - i
                full_left = min(left_choices, max(0, limit_sum - right_choices))
                count = full_left * right_choices
                low = full_left + 1
                high = min(left_choices, limit_sum - 1)
                if low <= high:
                    terms = high - low + 1
                    count += terms * limit_sum - (low + high) * terms // 2
                result[i] = count
            return result

        minimum_counts = counts_for_extreme(True)
        maximum_counts = counts_for_extreme(False)
        return sum(nums[i] * (minimum_counts[i] + maximum_counts[i]) for i in range(n))