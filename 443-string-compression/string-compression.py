
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Two pointers
        # read scans groups
        # write overwrites array with compressed output
        n = len(chars)
        write = 0
        read = 0

        while read < n:
            ch = chars[read]
            start = read

            # Advance read to end of current group
            while read < n and chars[read] == ch:
                read += 1

            count = read - start

            # Write the character
            chars[write] = ch
            write += 1

            # Write the count digits if greater than one
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
