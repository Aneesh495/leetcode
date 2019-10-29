
from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Breadth first search over gene strings
        # Each edge is a single character change that results in a string from the bank
        if startGene == endGene:
            return 0

        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        letters = ("A", "C", "G", "T")
        q = deque([(startGene, 0)])
        visited = set([startGene])

        while q:
            gene, steps = q.popleft()
            if gene == endGene:
                return steps

            gene_list = list(gene)
            for i, orig in enumerate(gene_list):
                for ch in letters:
                    if ch == orig:
                        continue
                    gene_list[i] = ch
                    nxt = "".join(gene_list)
                    if nxt in bank_set and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))
                gene_list[i] = orig  # restore for next position

        return -1
