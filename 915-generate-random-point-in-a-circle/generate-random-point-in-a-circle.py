
import random
import math
from typing import List

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        theta = 2 * math.pi * random.random()
        u = random.random()
        rr = self.r * math.sqrt(u)
        x = self.xc + rr * math.cos(theta)
        y = self.yc + rr * math.sin(theta)
        return [x, y]
