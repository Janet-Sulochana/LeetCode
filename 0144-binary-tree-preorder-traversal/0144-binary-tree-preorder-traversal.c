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
void preorderRecur(struct TreeNode* root,int *result,int *index){
    if(root==NULL)return;
    result[(*index)++]=root->val;
    preorderRecur(root->left,result,index);
    preorderRecur(root->right,result,index);
}

int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    int *result=(int*)malloc(sizeof(int)*1000);
    *returnSize=0;
    preorderRecur(root,result,returnSize);
    return result;
}