
from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        # Count all letters in the input
        freq = Counter(s)

        # Each digit word. Use letters that are unique to a digit first
        # zero z. two w. four u. six x. eight g
        cnt = [0] * 10
        cnt[0] = freq['z']
        cnt[2] = freq['w']
        cnt[4] = freq['u']
        cnt[6] = freq['x']
        cnt[8] = freq['g']

        # Resolve the remaining digits by subtracting already accounted letters
        # three h after removing eight
        cnt[3] = freq['h'] - cnt[8]
        # five f after removing four
        cnt[5] = freq['f'] - cnt[4]
        # seven s after removing six
        cnt[7] = freq['s'] - cnt[6]
        # one o after removing zero two four
        cnt[1] = freq['o'] - cnt[0] - cnt[2] - cnt[4]
        # nine i after removing five six eight
        cnt[9] = freq['i'] - cnt[5] - cnt[6] - cnt[8]

        # Build the answer in ascending order
        ans = []
        for d in range(10):
            if cnt[d] > 0:
                ans.append(str(d) * cnt[d])

        return ''.join(ans)
