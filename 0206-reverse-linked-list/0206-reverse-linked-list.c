/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    int values[10000];
    int size=0;
    struct ListNode *curr=head;
    while(curr!=NULL)
    {
        values[size]=curr->val;
        curr=curr->next;
        size++;
    }
    for(int i=0;i<size/2;i++)
    {
        int temp=values[i];
        values[i]=values[size-1-i];
        values[size-1-i]=temp;
    }
    curr=head;
    for(int i=0;i<size;i++)
    {
        curr->val=values[i];
        curr=curr->next;
    }
    return head;
}