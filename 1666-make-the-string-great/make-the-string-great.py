class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            # Uppercase and lowercase forms of an ASCII letter differ by 32.
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)