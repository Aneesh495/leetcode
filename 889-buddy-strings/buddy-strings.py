
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Lengths must match
        if len(s) != len(goal):
            return False

        # If equal we need a duplicate character to swap and stay equal
        if s == goal:
            seen = set()
            for ch in s:
                if ch in seen:
                    return True
                seen.add(ch)
            return False

        # Collect mismatch pairs
        diffs = []
        for a, b in zip(s, goal):
            if a != b:
                diffs.append((a, b))
                if len(diffs) > 2:
                    return False

        # Exactly two mismatches and they cross match
        return len(diffs) == 2 and diffs[0] == (diffs[1][1], diffs[1][0])
