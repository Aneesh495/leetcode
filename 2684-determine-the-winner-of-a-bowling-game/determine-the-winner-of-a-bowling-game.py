class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(player: List[int]) -> int:
            total = 0
            for i, pins in enumerate(player):
                doubled = (i >= 1 and player[i - 1] == 10) or (i >= 2 and player[i - 2] == 10)
                total += pins * (2 if doubled else 1)
            return total

        first = score(player1)
        second = score(player2)
        return 1 if first > second else (2 if second > first else 0)