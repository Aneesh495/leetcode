class Solution:
    def maxLength(self, arr: list[str]) -> int:
        states = [0]
        for word in arr:
            mask = 0
            valid = True
            for ch in word:
                bit = 1 << (ord(ch) - ord('a'))
                if mask & bit:
                    valid = False
                    break
                mask |= bit
            if not valid:
                continue
            additions = [used | mask for used in states if not (used & mask)]
            states.extend(additions)
        return max(mask.bit_count() for mask in states)