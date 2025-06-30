/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    int values[10000];
    int size=0;
    struct ListNode *cur=head;
    while(cur!=NULL)
    {
        values[size]=cur->val;
        cur=cur->next;
        size++;
    }
    int i=left-1;
    int j=right-1;
    while(i<j)
    {
        int temp=values[i];
        values[i]=values[j];
        values[j]=temp;   
        i++;
        j--; 
    }
    cur=head;
    int k=0;
    while(cur!=NULL)
    {
        cur->val=values[k];
        k++;
        cur=cur->next;
    }
    return head;
}