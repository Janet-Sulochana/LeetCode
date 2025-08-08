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
    while(first!=NULL)
    {
        struct ListNode *second=headB;
        while(second!=NULL)
        {
            if(first==second)
            {
                return first;
            }
            second=second->next;
        }
        first=first->next;
    }
    return 0;
}