
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            ident, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digits.append(log)
            else:
                letters.append((rest, ident, log))
        letters.sort(key=lambda x: (x[0], x[1]))
        return [x[2] for x in letters] + digits
