
from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_block = False
        buf = []

        for line in source:
            i = 0
            if not in_block:
                buf = []
            n = len(line)
            while i < n:
                if not in_block and i + 1 < n and line[i] == '/' and line[i + 1] == '/':
                    break
                if not in_block and i + 1 < n and line[i] == '/' and line[i + 1] == '*':
                    in_block = True
                    i += 2
                    continue
                if in_block and i + 1 < n and line[i] == '*' and line[i + 1] == '/':
                    in_block = False
                    i += 2
                    continue
                if not in_block:
                    buf.append(line[i])
                i += 1
            if not in_block and buf:
                res.append(''.join(buf))
        return res
