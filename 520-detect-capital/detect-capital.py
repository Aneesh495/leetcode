
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        Return True if capitalization is correct:
        1) All letters uppercase like 'USA'
        2) All letters lowercase like 'leetcode'
        3) Only first letter uppercase like 'Google'
        """
        # Check the three valid patterns directly using built-in string methods
        return (
            word.isupper()               # all caps
            or word.islower()            # all lowercase
            or (word[0].isupper() and word[1:].islower())  # first cap rest lower
        )
