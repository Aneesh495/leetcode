
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # Sort then interleave reversed halves to enforce nums[0] < nums[1] > nums[2] < nums[3] ...
        n = len(nums)
        arr = sorted(nums)
        mid = (n + 1) // 2                        # left half length
        left = arr[:mid][::-1]                    # largest of left half first
        right = arr[mid:][::-1]                   # largest of right half first

        # Fill back in alternating order
        i = j = 0
        for k in range(n):
            if k % 2 == 0:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
