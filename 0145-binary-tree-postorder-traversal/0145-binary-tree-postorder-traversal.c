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
void postTraverse(struct TreeNode* root, int result[], int* n)
{
    if(root==NULL)return;

    postTraverse(root->left,result,n);
    postTraverse(root->right,result,n);
    result[(*n)++]=root->val;
}
int* postorderTraversal(struct TreeNode* root, int* returnSize) {
    int n=0;
    int *result=(int*)malloc(sizeof(int)*1000);
    postTraverse(root,result,&n);
    *returnSize=n;
    return result;
}