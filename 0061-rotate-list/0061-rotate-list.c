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
    current = head;
    for(int i=1;i<count-k;i++)
    {
        current=current->next;
    }
    struct ListNode *newhead=current->next;
    current->next=NULL;
    struct ListNode *tail=newhead;
    while(tail->next!=NULL)
    {
        tail=tail->next;
    }
    tail->next=head;
    return newhead;
}