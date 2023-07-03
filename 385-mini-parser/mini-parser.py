
# LeetCode 385. Mini Parser
# Implement only the required function. The NestedInteger class is provided by LeetCode.

class Solution:
    def deserialize(self, s: str) -> 'NestedInteger':
        # If the input is a single integer return it directly
        if not s:
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        
        # Use a stack of NestedInteger to build nested lists
        stack = []
        num = None          # current number being parsed
        sign = 1            # sign for the current number
        
        for ch in s:
            if ch == '[':
                # Start a new list and push onto stack
                stack.append(NestedInteger())
                num = None
                sign = 1
            elif ch == '-':
                # Next number is negative
                sign = -1
            elif ch.isdigit():
                # Build the current number
                if num is None:
                    num = 0
                num = num * 10 + int(ch)
            elif ch in ',]':
                # If we have a number buffered add it to the top list
                if num is not None:
                    stack[-1].add(NestedInteger(sign * num))
                    num = None
                    sign = 1
                # If we close a list and there is a parent list add it upward
                if ch == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)
        
        # The whole structure is the only element left on the stack
        return stack[-1] if stack else NestedInteger()
