
class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@', 1)
            return name[0] + "*****" + name[-1] + "@" + domain
        digits = [c for c in s if c.isdigit()]
        last4 = "".join(digits[-4:])
        country = len(digits) - 10
        base = "***-***-" + last4
        if country <= 0:
            return base
        return "+" + "*" * country + "-" + base
