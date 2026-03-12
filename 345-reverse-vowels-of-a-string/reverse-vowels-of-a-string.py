
class Solution:
    def reverseVowels(self, s: str) -> str:
        # Use two pointers that move toward each other
        vowels = set("aeiouAEIOU")
        chars = list(s)                     # Strings are immutable so work on a list
        i, j = 0, len(chars) - 1

        while i < j:
            # Advance left pointer until it finds a vowel
            while i < j and chars[i] not in vowels:
                i += 1
            # Advance right pointer until it finds a vowel
            while i < j and chars[j] not in vowels:
                j -= 1
            # Swap the vowels
            if i < j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1

        return "".join(chars)
