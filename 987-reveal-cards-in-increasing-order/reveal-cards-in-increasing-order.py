
from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort cards so we place them from smallest to largest
        deck.sort()
        n = len(deck)

        # Simulate reveal using index positions
        # idx holds positions in the output deck that will be filled next
        idx = deque(range(n))
        ans = [0] * n

        for card in deck:
            # Reveal top position and place current smallest card there
            pos = idx.popleft()
            ans[pos] = card

            # Move next top index to bottom if any remain
            if idx:
                idx.append(idx.popleft())

        return ans
