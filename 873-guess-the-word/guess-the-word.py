class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def matches(a, b):
            return sum(x == y for x, y in zip(a, b))

        candidates = words[:]
        while candidates:
            best, best_worst = candidates[0], len(candidates)
            for word in candidates:
                buckets = [0] * 6
                for other in candidates:
                    if other != word:
                        buckets[matches(word, other)] += 1
                worst = max(buckets)
                if worst < best_worst:
                    best, best_worst = word, worst
            score = master.guess(best)
            if score == 6:
                return
            candidates = [w for w in candidates if matches(best, w) == score]
