
# The guess API is already defined for you
# def guess(num: int) -> int:
# returns -1 if num is higher than the picked number
# returns 1 if num is lower than the picked number
# returns 0 if num equals the picked number

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2  # avoid potential overflow in other languages
            res = guess(mid)
            if res == 0:
                return mid  # found the picked number
            if res < 0:
                right = mid - 1  # mid is higher than pick
            else:
                left = mid + 1  # mid is lower than pick
        return -1  # unreachable given valid constraints
