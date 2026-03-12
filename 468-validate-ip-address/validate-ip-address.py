
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # Main dispatcher
        if queryIP.count('.') == 3 and queryIP.count(':') == 0:
            return "IPv4" if self._is_ipv4(queryIP) else "Neither"
        if queryIP.count(':') == 7 and queryIP.count('.') == 0:
            return "IPv6" if self._is_ipv6(queryIP) else "Neither"
        return "Neither"

    def _is_ipv4(self, s: str) -> bool:
        # IPv4 must have 4 decimal blocks separated by periods
        parts = s.split('.')
        if len(parts) != 4:
            return False
        for p in parts:
            # Each part must be nonempty
            if len(p) == 0:
                return False
            # No leading zeros unless the part is exactly "0"
            if len(p) > 1 and p[0] == '0':
                return False
            # Only digits allowed
            if not p.isdigit():
                return False
            # Numeric range 0 to 255
            try:
                val = int(p)
            except ValueError:
                return False
            if val < 0 or val > 255:
                return False
        return True

    def _is_ipv6(self, s: str) -> bool:
        # IPv6 must have 8 hexadecimal blocks separated by colons
        parts = s.split(':')
        if len(parts) != 8:
            return False
        hexdigits = set("0123456789abcdefABCDEF")
        for p in parts:
            # Each block length 1 to 4
            if len(p) == 0 or len(p) > 4:
                return False
            # Hex digits only
            if any(ch not in hexdigits for ch in p):
                return False
        return True
