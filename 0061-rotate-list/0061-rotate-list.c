/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    while(head==NULL || head->next==NULL || k==0)
    {
        return head;
    }
    int count=0;
    struct ListNode *current=head;
    while(current!=NULL)
    {
        count++;
        current=current->next;
    }
    for(int i=0;i<k;i++)
    {
        struct ListNode *prev=NULL;
        struct ListNode *tail=head;
        while(tail->next!=NULL)
        {
            prev=tail;
            tail=tail->next;
        }
        if(prev!=NULL)
        {
            prev->next=NULL;
            tail->next=head;
            head=tail;
        }
    }
    return head;
}