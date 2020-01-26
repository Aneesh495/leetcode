
class Solution:
    def checkRecord(self, s: str) -> bool:
        # Eligible if absences are fewer than 2
        # And no 3 consecutive late days occur
        return s.count('A') < 2 and 'LLL' not in s
