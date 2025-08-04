/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    while(head==NULL||head->next==NULL)return head;
    struct ListNode* temp1=head;
    struct ListNode* temp2=NULL;
    struct ListNode* newHead=NULL;
    while(temp1!=NULL)
    {
        bool isDup=false;
        while(temp1->next!=NULL&&temp1->val==temp1->next->val)
        {
            isDup=true;
            struct ListNode* temp=temp1;
            temp1=temp1->next;
            free(temp);
        }
        if(!isDup)
        {
            if(temp2==NULL)
                newHead=temp1;
            else
                temp2->next=temp1;
            temp2=temp1;
            temp1=temp1->next;
        }
        else
        {
            struct ListNode* temp=temp1;
            temp1=temp1->next;
            free(temp);
        }
    }
    if(temp2!=NULL) temp2->next=NULL;
    return newHead;
}