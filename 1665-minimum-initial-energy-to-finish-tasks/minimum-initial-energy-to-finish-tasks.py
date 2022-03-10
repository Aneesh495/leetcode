class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda t: t[1]-t[0], reverse=True)
        spent = answer = 0
        for actual, minimum in tasks:
            answer = max(answer, spent+minimum)
            spent += actual
        return answer