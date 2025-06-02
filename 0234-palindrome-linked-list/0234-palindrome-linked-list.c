/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    struct ListNode *current=head;
    int values[100000];
    int size=0;
    while(current!=NULL)
    {
        values[size]=current->val;
        current=current->next;
        size++;
    }
    for(int i=0;i<size/2;i++)
    {
        if(values[i]!=values[size-i-1])
        {
            return false;
        }
    }
    return true;

}