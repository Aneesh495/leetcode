
class Solution:
    def deleteNode(self, node):
        # Copy value from next node into current node
        node.val = node.next.val
        # Skip over the next node to delete it
        node.next = node.next.next
