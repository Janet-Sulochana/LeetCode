/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#define MAX 100
void inorder(struct TreeNode* root, int result[], int *n)
{
    if(root==NULL)return;
    inorder(root->left,result,n);
    result[(*n)++]=root->val;
    inorder(root->right,result,n);
}
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int n=0;
    int *result=(int*)malloc(MAX * sizeof(struct TreeNode));
    inorder(root,result,&n);
    *returnSize=n;
    return result;
}
