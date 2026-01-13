/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    if(head==NULL)return NULL;
    if(head!=NULL && head->val==val){
        struct ListNode* temp=head;
        head=head->next;
        free(temp);
    }
        
    struct ListNode* curr=head;
    while(curr!=NULL && curr->next!=NULL){
        if(curr->next->val == val){
            struct ListNode* temp=curr->next;
            curr->next=curr->next->next;
            free(temp);
        }
        else curr=curr->next;
    }
    if(head!=NULL && head->val==val){
        struct ListNode* temp=head;
        head=head->next;
        free(temp);
    }
    return head;

}