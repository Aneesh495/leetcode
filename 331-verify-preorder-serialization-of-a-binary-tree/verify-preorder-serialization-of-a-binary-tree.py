
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Use slot counting
        # Start with one slot for the root
        slots = 1
        for token in preorder.split(','):
            # One slot is consumed by the current node
            slots -= 1
            if slots < 0:
                return False
            # Non null node creates two new slots for its children
            if token != '#':
                slots += 2
        # All slots must be exactly filled
        return slots == 0
