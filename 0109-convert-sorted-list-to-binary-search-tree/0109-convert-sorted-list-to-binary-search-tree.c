/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* sortedListToBST(struct ListNode* head) {
    if(head==NULL)return NULL;
    if(head->next==NULL){
        struct TreeNode* root=(struct TreeNode*)malloc(sizeof(struct TreeNode));
        root->val=head->val;
        root->left=NULL;
        root->right=NULL;
    }
    struct ListNode* fast=head;
    struct ListNode* slow=head;
    struct ListNode* prev=NULL;
    while(fast!=NULL && fast->next!=NULL)
    {
        prev=slow;
        slow=slow->next;
        fast=fast->next->next;
    }
    
    struct TreeNode* root=(struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val=slow->val;
    if(prev!=NULL){
        prev->next=NULL;
        root->left=sortedListToBST(head);
    }
    else{
        root->left=NULL;
    }
    root->right=sortedListToBST(slow->next);
    return root;
}