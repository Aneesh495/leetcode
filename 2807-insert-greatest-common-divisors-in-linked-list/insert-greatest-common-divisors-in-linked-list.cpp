class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* cur = head;
        while (cur && cur->next) {
            ListNode* node = new ListNode(gcd(cur->val, cur->next->val), cur->next);
            cur->next = node;
            cur = node->next;
        }
        return head;
    }
};
