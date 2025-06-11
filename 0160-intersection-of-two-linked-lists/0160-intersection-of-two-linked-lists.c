/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if(headA==NULL || headB==NULL)
    return NULL;
    struct ListNode *first=headA;
    struct ListNode *second=headB;
    while(first!=second)
    {
        first=(first==NULL)?headB:first->next;
        second=(second==NULL)?headA:second->next;
    }
    return first;
}