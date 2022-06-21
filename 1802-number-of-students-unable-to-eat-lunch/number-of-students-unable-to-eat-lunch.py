class Solution:
    def countStudents(self, students, sandwiches):
        counts=[students.count(0),students.count(1)]
        for s in sandwiches:
            if not counts[s]: break
            counts[s]-=1
        return sum(counts)