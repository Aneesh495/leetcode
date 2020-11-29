
from fractions import Fraction

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        # Convert a decimal string with optional repeating part into an exact Fraction
        def to_fraction(x: str) -> Fraction:
            # Split repeating part if present
            if '(' in x:
                pre, rep = x.split('(')
                rep = rep[:-1]  # drop ')'
            else:
                pre, rep = x, ""

            # Split integer and non-repeating fractional part
            if '.' in pre:
                int_part_str, nonrep_str = pre.split('.')
            else:
                int_part_str, nonrep_str = pre, ""

            I = int(int_part_str) if int_part_str else 0
            k = len(nonrep_str)
            nr = int(nonrep_str) if nonrep_str else 0

            # Non-repeating contribution
            frac = Fraction(nr, 10 ** k)

            # Repeating contribution
            if rep:
                m = len(rep)
                rp = int(rep)
                # value of repeating block: rp / (10^k * (10^m - 1))
                frac += Fraction(rp, (10 ** k) * (10 ** m - 1))

            return Fraction(I, 1) + frac

        return to_fraction(s) == to_fraction(t)
