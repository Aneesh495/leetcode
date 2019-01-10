from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Return empty list for empty input
        if not digits:
            return []

        # Map each digit to its letters
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res: List[str] = []
        path: List[str] = []

        # Standard backtracking that builds one path at a time
        def dfs(i: int) -> None:
            # Reached full length so record the path
            if i == len(digits):
                res.append("".join(path))
                return
            # Try each letter for the current digit
            for ch in phone[digits[i]]:
                path.append(ch)
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res