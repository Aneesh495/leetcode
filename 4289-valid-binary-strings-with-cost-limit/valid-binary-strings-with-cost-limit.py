class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        answer = []

        def generate(index, remaining, last_one, prefix):
            if index == n:
                answer.append(prefix)
                return
            generate(index + 1, remaining, False, prefix + '0')
            # Placing a one uses its index as the cost and breaks the next one's eligibility.
            if not last_one and index <= remaining:
                generate(index + 1, remaining - index, True, prefix + '1')

        generate(0, k, False, '')
        return answer