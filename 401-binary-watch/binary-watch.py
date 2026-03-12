
from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def ones(x: int) -> int:
            try:
                return x.bit_count()
            except AttributeError:
                return bin(x).count("1")
        res = []
        for h in range(12):
            for m in range(60):
                if ones(h) + ones(m) == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res
