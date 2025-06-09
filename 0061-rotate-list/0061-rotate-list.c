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
    k=k%count;
    if(k==0) return head;
    for(int i=0;i<k;i++)
    {
        struct ListNode *current=head;
        struct ListNode *prev=NULL;
        while(current->next!=NULL)
        {
            prev=current;
            current=current->next;
        }
        if(prev!=NULL)
        {
            prev->next=NULL;
            current->next=head;
            head=current;
        }
    }
    return head;
}