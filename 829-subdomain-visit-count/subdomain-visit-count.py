
from typing import List
from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = Counter()
        for entry in cpdomains:
            c_str, domain = entry.split()
            c = int(c_str)
            parts = domain.split(".")
            for i in range(len(parts)):
                sub = ".".join(parts[i:])
                counts[sub] += c
        return [f"{v} {k}" for k, v in counts.items()]
