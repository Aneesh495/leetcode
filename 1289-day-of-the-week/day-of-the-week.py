class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def is_leap(y: int) -> bool:
            return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

        total = 0

        for y in range(1971, year):
            total += 366 if is_leap(y) else 365

        for m in range(1, month):
            total += month_days[m - 1]
            if m == 2 and is_leap(year):
                total += 1

        total += day - 1

        return days[(5 + total) % 7]
