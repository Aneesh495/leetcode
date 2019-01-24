
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Use a stack of indices to mark the last unmatched position
        # Start with sentinel index for the base of the first valid block
        stack = [-1]
        best = 0

        for i, ch in enumerate(s):
            if ch == '(':
                # Push index of every open
                stack.append(i)
            else:
                # Try to match a previous open
                stack.pop()
                if not stack:
                    # No open to match so set new base at this close
                    stack.append(i)
                else:
                    # Length of current valid block equals i minus last unmatched index
                    best = max(best, i - stack[-1])

        return best