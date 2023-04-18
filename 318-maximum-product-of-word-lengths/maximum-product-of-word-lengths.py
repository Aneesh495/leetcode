
class Solution:
    def maxProduct(self, words: list[str]) -> int:
        # Build a bitmask for each word
        # Store only the longest length seen for a given mask
        mask_len = {}
        for w in words:
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - 97)
            if m in mask_len:
                if len(w) > mask_len[m]:
                    mask_len[m] = len(w)
            else:
                mask_len[m] = len(w)

        # Compare masks that share no letters
        ans = 0
        items = list(mask_len.items())
        n = len(items)
        for i in range(n):
            m1, l1 = items[i]
            for j in range(i + 1, n):
                m2, l2 = items[j]
                if m1 & m2 == 0:
                    prod = l1 * l2
                    if prod > ans:
                        ans = prod
        return ans
