
class Solution:
    def countSegments(self, s: str) -> int:
        # Count segments by detecting transitions from space to non space
        count = 0
        in_seg = False  # True if we are inside a segment
        for ch in s:
            if ch != ' ':
                if not in_seg:
                    count += 1  # Start of a new segment
                    in_seg = True
            else:
                in_seg = False  # End current segment
        return count
