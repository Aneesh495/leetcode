
from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        need = 0
        for b in data:
            b &= 255
            if need == 0:
                mask = 128
                count = 0
                while b & mask:
                    count += 1
                    mask >>= 1
                if count == 0:
                    continue
                if count == 1 or count > 4:
                    return False
                need = count - 1
            else:
                if (b & 192) != 128:
                    return False
                need -= 1
        return need == 0
