
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Iterative DFS using a stack
        Splice each child list between the node and its original next
        Maintain prev and next pointers
        Set child to None after splicing
        """
        if not head:
            return head

        # Pseudo head simplifies edge cases at the real head
        pseudo = Node(0, None, head, None)
        prev = pseudo

        stack = [head]
        while stack:
            curr = stack.pop()

            # Link prev <-> curr
            prev.next = curr
            curr.prev = prev

            # Push next first so child is processed before it
            if curr.next:
                stack.append(curr.next)

            # Child goes on stack to be processed next
            if curr.child:
                stack.append(curr.child)
                curr.child = None  # required by problem

            prev = curr

        # Detach the pseudo head
        pseudo.next.prev = None
        return pseudo.next
