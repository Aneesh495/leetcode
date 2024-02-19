
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for i in range(n):
            cnt1[ord(s1[i]) - 97] += 1
            cnt2[ord(s2[i]) - 97] += 1

        matches = sum(1 for i in range(26) if cnt1[i] == cnt2[i])

        for i in range(n, m):
            if matches == 26:
                return True

            idx_in = ord(s2[i]) - 97
            idx_out = ord(s2[i - n]) - 97

            cnt2[idx_in] += 1
            if cnt2[idx_in] == cnt1[idx_in]:
                matches += 1
            elif cnt2[idx_in] - 1 == cnt1[idx_in]:
                matches -= 1

            cnt2[idx_out] -= 1
            if cnt2[idx_out] == cnt1[idx_out]:
                matches += 1
            elif cnt2[idx_out] + 1 == cnt1[idx_out]:
                matches -= 1

        return matches == 26
