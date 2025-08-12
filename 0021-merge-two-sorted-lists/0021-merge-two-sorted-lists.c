/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if(list1==NULL)return list2;
    if(list2==NULL)return list1;
    struct ListNode *head=malloc(sizeof(struct ListNode));
    struct ListNode *temp=head;
    while(list1!=NULL && list2!=NULL)
    {
        if(list1->val<=list2->val)
        {
            temp->val=list1->val;
            list1=list1->next;
        }
        else
        {
            temp->val=list2->val;
            list2=list2->next;
        }
        if(list1!=NULL && list2!=NULL)
        {
            temp->next=malloc(sizeof(struct ListNode));
            temp=temp->next;
        }
    }
    if(list1!=NULL)
    {
        temp->next=list1;
    }
    else
    {
        temp->next=list2;
    }
    return head;
}