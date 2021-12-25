class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result, current = [], 1
        for x in target:
            while current < x:
                result.extend(("Push", "Pop"))
                current += 1
            result.append("Push")
            current += 1
        return result