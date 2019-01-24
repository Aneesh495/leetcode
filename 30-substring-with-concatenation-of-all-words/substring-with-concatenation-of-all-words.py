

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Guard cases
        if not s or not words:
            return []
        wlen = len(words[0])
        nwords = len(words)
        tot = wlen * nwords
        if len(s) < tot:
            return []

        need = Counter(words)          # target word multiset
        res: List[int] = []

        # Try windows that start at each offset modulo word length
        for offset in range(wlen):
            left = offset              # start of current window
            count = 0                  # number of words in current window
            have = Counter()           # counts of words inside window

            # step through s in word sized jumps
            for right in range(offset, len(s) - wlen + 1, wlen):
                word = s[right:right + wlen]

                if word in need:
                    have[word] += 1
                    count += 1

                    # If this word is over the allowed count then shrink from the left
                    while have[word] > need[word]:
                        left_word = s[left:left + wlen]
                        have[left_word] -= 1
                        left += wlen
                        count -= 1

                    # If window has all words then record start and slide by one word
                    if count == nwords:
                        res.append(left)
                        left_word = s[left:left + wlen]
                        have[left_word] -= 1
                        left += wlen
                        count -= 1
                else:
                    # Reset window when encountering a word not in need
                    have.clear()
                    count = 0
                    left = right + wlen

        return res
