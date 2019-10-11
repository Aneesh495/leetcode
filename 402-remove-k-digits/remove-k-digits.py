
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Use a monotonic increasing stack to keep the number as small as possible
        stack = []

        for ch in num:
            # Pop larger previous digits while we can remove more
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # If we still have removals left remove from the end
        if k > 0:
            stack = stack[:-k] if k <= len(stack) else []

        # Build result and strip leading zeros
        res = ''.join(stack).lstrip('0')

        # If everything removed or only zeros return "0"
        return res if res else "0"
