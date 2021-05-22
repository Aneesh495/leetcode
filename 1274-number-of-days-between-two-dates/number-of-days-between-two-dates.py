class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def ordinal(date: str) -> int:
            year, month, day = map(int, date.split('-'))
            leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
            month_days = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            previous_year = year - 1
            total = 365 * previous_year + previous_year // 4 - previous_year // 100 + previous_year // 400
            return total + sum(month_days[:month - 1]) + day

        return abs(ordinal(date1) - ordinal(date2))