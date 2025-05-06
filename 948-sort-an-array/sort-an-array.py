
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(a, l, r, tmp):
            if r - l <= 1:
                return
            m = (l + r) // 2
            merge_sort(a, l, m, tmp)
            merge_sort(a, m, r, tmp)
            i, j, k = l, m, l
            while i < m and j < r:
                if a[i] <= a[j]:
                    tmp[k] = a[i]
                    i += 1
                else:
                    tmp[k] = a[j]
                    j += 1
                k += 1
            while i < m:
                tmp[k] = a[i]
                i += 1
                k += 1
            while j < r:
                tmp[k] = a[j]
                j += 1
                k += 1
            for t in range(l, r):
                a[t] = tmp[t]

        tmp = [0] * len(nums)
        merge_sort(nums, 0, len(nums), tmp)
        return nums
