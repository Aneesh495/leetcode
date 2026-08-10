class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        left = 0
        right = n - 1
        chunks = 0
        while left <= right:
            candidate_length = 1
            while (
                left + candidate_length - 1 < right - candidate_length + 1
                and text[left:left + candidate_length]
                != text[right - candidate_length + 1:right + 1]
            ):
                candidate_length += 1
            if (
                left + candidate_length -1 < right - candidate_length + 1
                and text[left:left + candidate_length]
                == text[right - candidate_length +1:right + 1]
            ):
                chunks += 2
                left += candidate_length
                right -= candidate_length
            else:
                chunks += 1
                break
        return chunks