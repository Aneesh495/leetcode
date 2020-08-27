
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        fleets = 0
        cur_time = 0.0
        for pos, spd in cars:
            t = (target - pos) / spd
            if t > cur_time:
                fleets += 1
                cur_time = t
        return fleets
