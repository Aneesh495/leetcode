
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        """
        Count how many times s2 repeated n2 can be obtained from s1 repeated n1
        Treat both as infinite sequences built by concatenation
        Match s2 as a subsequence while scanning repeated s1
        Use cycle detection on the pointer j in s2 to jump over repeating patterns
        """

        # Quick reject if s2 contains a char not in s1
        if set(s2) - set(s1):
            return 0

        # count[k] = total number of completed s2 blocks after finishing k blocks of s1
        # seen[j] = first s1 block index where s2 pointer j was observed
        count = [0] * (n1 + 1)
        seen = {}

        j = 0  # pointer in s2
        for i in range(1, n1 + 1):
            # scan one block of s1
            for ch in s1:
                if ch == s2[j]:
                    j += 1
                    if j == len(s2):
                        j = 0
                        count[i] += 1
            count[i] += count[i - 1]

            # if we have seen this j before, a cycle is found
            if j in seen:
                # cycle spans from prev to i
                prev = seen[j]
                pre_count = count[prev]
                cycle_len = i - prev
                cycle_count = count[i] - count[prev]

                # how many full cycles fit in the remaining blocks
                remaining = n1 - prev
                full_cycles = remaining // cycle_len

                # total s2 blocks equals pre part plus cycles plus tail part
                total = pre_count + full_cycles * cycle_count
                tail = remaining % cycle_len
                total += count[prev + tail] - count[prev]

                return total // n2
            else:
                seen[j] = i

        # no cycle detected within n1 blocks
        return count[n1] // n2
