class Solution:
    def isValid(self, s: str) -> bool:
        """
        Validate a string of brackets using a stack
        Rules
          1 open brackets must be closed by the same type
          2 order must be correct
          3 every close must have a matching open
        Time O(n) where n is len(s)
        Space O(n) for the stack
        """
        if len(s) % 2 == 1:
            return False  # odd length can never be fully matched

        match = {')': '(', ']': '[', '}': '{'}
        opens = set(match.values())
        stack = []

        for ch in s:
            if ch in opens:
                stack.append(ch)  # push open bracket
            elif ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False  # no open to match or wrong type
                stack.pop()  # matched pair
            else:
                return False  # invalid character not expected by problem

        return not stack  # valid only if no unmatched opens remain