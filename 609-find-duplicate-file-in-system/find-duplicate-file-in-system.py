
from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)
        for entry in paths:
            parts = entry.split()
            directory = parts[0]
            for file_part in parts[1:]:
                l = file_part.find('(')
                r = file_part.rfind(')')
                filename = file_part[:l]
                content = file_part[l+1:r]
                full_path = f"{directory}/{filename}"
                content_map[content].append(full_path)
        return [v for v in content_map.values() if len(v) > 1]
