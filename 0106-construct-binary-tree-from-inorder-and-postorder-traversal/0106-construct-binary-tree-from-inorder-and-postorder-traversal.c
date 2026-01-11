/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int search(int* inorder, int start, int end, int key){
    for(int i=start;i<=end;i++){
        if(inorder[i]==key)
            return i;
    }
    return -1;
 }
struct TreeNode* build(int* postorder,int* inorder,int start, int end, int* postIndex){
    if(start>end)return NULL;

    struct TreeNode* root=(struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val=postorder[*postIndex];
    (*postIndex)--;
    root->left=NULL;
    root->right=NULL;

    if(start==end)return root;

    int inIndex= search(inorder,start,end,root->val);
    if(inIndex==-1)return NULL;

    root->right=build(postorder,inorder,inIndex+1,end,postIndex);
    root->left=build(postorder,inorder,start,inIndex-1,postIndex);
    return root;
}
struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize) {
    if(postorderSize==0 || postorderSize!=inorderSize)return NULL;
    int postIndex=postorderSize-1;
    return build(postorder,inorder,0,inorderSize-1,&postIndex);
}