from typing import List

class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n = len(nums)
        previous = [0, 0]
        for i in range(n):
            current = [float("-inf"), float("-inf")]
            choices = (0, 1) if s[i] == "1" else (0,)

            for current_choice in choices:
                for previous_choice in (0, 1):
                    covered_previous = (
                        i > 0
                        and (
                            (s[i - 1] == "1" and previous_choice == 0)
                            or current_choice == 1
                        )
                    )
                    value = previous[previous_choice]
                    if covered_previous:
                        value += nums[i - 1]
                    
                    current[current_choice] = max(
                        current[current_choice],
                        value,
                    )
            previous = current
        answer = 0
        for final_choice in (0, 1):
            value = previous[final_choice]
            if s[n - 1] == "1" and final_choice == 0:
                value += nums[n - 1]
            answer = max(answer, value)
        return answer