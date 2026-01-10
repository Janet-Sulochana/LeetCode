/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int search(int *inorder,int start,int end,int key){
    for(int i=start;i<=end;i++){
        if(inorder[i]==key)
            return i;
    }
    return -1;
}

struct TreeNode* build(int *preorder,int *inorder,int start, int end,int *preIndex){
    
    if(start>end)return NULL;

    struct TreeNode* root=(struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val=preorder[*preIndex];
    (*preIndex)++;
    root->left=NULL;
    root->right=NULL;

    if(start==end)return root;

    int inIndex=search(inorder,start,end,root->val);

    if(inIndex==-1)return NULL;
    root->left=build(preorder,inorder,start,inIndex-1,preIndex);
    root->right=build(preorder,inorder,inIndex+1,end,preIndex);

    return root;
}
struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
    if(preorderSize==0 || preorderSize!=inorderSize)return NULL;
    int preIndex=0;
    return build(preorder,inorder,0,inorderSize-1,&preIndex);
    
}