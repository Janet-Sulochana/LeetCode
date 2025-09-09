/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* deleteNode(struct TreeNode* root, int key) {
    if(root==NULL)return NULL;

    if(key<root->val)
    {
        root->left=deleteNode(root->left,key);
    }
    else if(key>root->val)
    {
        root->right=deleteNode(root->right,key);
    }
    else
    {
        if(root->left==NULL)
        {
            struct TreeNode* temp=root->right;
            free(root);
            return temp;
        }
        else if(root->right==NULL)
        {
            struct TreeNode* temp=root->left;
            free(root);
            return temp;
        }
        else{
            struct TreeNode* succ=root->right;
            while(succ->left)succ=succ->left;
            root->val=succ->val;
            root->right=deleteNode(root->right,succ->val);
        }
    }
    return root;
}