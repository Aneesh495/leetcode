
class Solution:
    def isValid(self, s: str) -> bool:
        """
        LeetCode 1003. Check If Word Is Valid After Substitutions
        Operation allowed: repeatedly insert substring "abc"
        A string is valid if it can be formed from empty string by inserting "abc" any number of times
        Equivalent check: scanning left to right and removing every completed "abc" in order
        Use a stack. Push chars. Whenever the last two are 'a' then 'b' and current char is 'c'
        pop twice and skip pushing 'c' which deletes one "abc"
        At the end the stack must be empty for validity
        Time O(n). Space O(n) worst case
        """
        st = []
        for ch in s:
            st.append(ch)
            # When we see the pattern "... a b c" collapse it
            if len(st) >= 3 and st[-3] == 'a' and st[-2] == 'b' and st[-1] == 'c':
                st.pop()   # remove 'c'
                st.pop()   # remove 'b'
                st.pop()   # remove 'a'
        return not st
