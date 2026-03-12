
import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        # Store the original array to allow exact reset
        self._original = nums[:]

    def reset(self) -> List[int]:
        # Return a fresh copy of the original state
        return self._original[:]

    def shuffle(self) -> List[int]:
        # Fisher Yates shuffle for uniform randomness
        arr = self._original[:]
        n = len(arr)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
