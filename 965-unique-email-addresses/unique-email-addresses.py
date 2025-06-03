
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for e in emails:
            local, domain = e.split('@', 1)
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)
