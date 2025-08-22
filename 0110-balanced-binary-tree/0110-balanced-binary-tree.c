/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int height(struct TreeNode* root){
    if(root==NULL)return 0;
    return 1+fmax(height(root->left),height(root->right));
}
bool isBalanced(struct TreeNode* root) {
    if(root==NULL)return true;
    int lheight=height(root->left);
    int rheight=height(root->right);
    if(abs(lheight-rheight)>1)return false;
    return (isBalanced(root->left)&&isBalanced(root->right));
}