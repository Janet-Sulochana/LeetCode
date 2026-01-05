/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* newNode(int val){
    struct TreeNode* Node=(struct TreeNode*)malloc(sizeof(struct TreeNode));
    Node->val=val;
    Node->left=NULL;
    Node->right=NULL;
    return Node;
} 
struct TreeNode* buildBST(int* nums,int left,int right){
    if(left>right)return NULL;
    int mid=left+(right-left)/2;
    struct TreeNode* root=newNode(nums[mid]);
    root->left=buildBST(nums,left,mid-1);
    root->right=buildBST(nums,mid+1,right);
    return root;
}
struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    if(numsSize==0)return NULL;
    return buildBST(nums,0,numsSize-1);
}