/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int len=0;
    struct ListNode *cur=head;
    while(cur!=NULL)
    {
        len++;
        cur=cur->next;
    }
    int position=len-n;
    if(position<0)
    {
        return head;
    }
    if(position==0)
    {
        struct ListNode *newhead=head->next;
        free(head);
        return newhead;
    }
    cur=head;
    for(int i=0;i<position-1;i++)
    {
        cur=cur->next;
    }
    struct ListNode *toDelete=cur->next;
    cur->next=toDelete->next;
    free(toDelete);
    return head;
}