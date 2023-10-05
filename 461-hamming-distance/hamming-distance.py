
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR sets bits where x and y differ
        z = x ^ y
        # Count set bits using Brian Kernighan’s algorithm
        count = 0
        while z:
            z &= z - 1  # clear the lowest set bit
            count += 1
        return count
