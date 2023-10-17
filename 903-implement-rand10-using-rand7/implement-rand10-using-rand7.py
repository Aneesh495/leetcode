
# The rand7() API is already defined for you.
# def rand7() -> int:

class Solution:
    def rand10(self) -> int:
        while True:
            a = rand7()
            b = rand7()
            idx = (a - 1) * 7 + b  # 1..49
            if idx <= 40:
                return 1 + (idx - 1) % 10

            idx -= 40  # 1..9
            a = rand7()
            idx = (idx - 1) * 7 + a  # 1..63
            if idx <= 60:
                return 1 + (idx - 1) % 10

            idx -= 60  # 1..3
            b = rand7()
            idx = (idx - 1) * 7 + b  # 1..21
            if idx <= 20:
                return 1 + (idx - 1) % 10
