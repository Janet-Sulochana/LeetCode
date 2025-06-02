/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** zigzagLevelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if(root==NULL)
    {
        *returnSize=0;
        *returnColumnSizes=NULL;
        return NULL;
    }
    struct TreeNode** queue=(struct TreeNode**)malloc(10000 * sizeof(struct TreeNode*));
    int front=0,rear=0;
    queue[rear++]=root;
    int **result=(int**)malloc(sizeof(int*));
    *returnSize=0;
    *returnColumnSizes=malloc(sizeof(int));
    int leftToRight=1;
    while(front<rear)
    {
        int levelSize=rear-front;
        int *levelNodes=(int*)malloc(levelSize * sizeof(int));
        for(int i=0;i<levelSize;i++)
        {
            struct TreeNode *node=queue[front++];
            int index=leftToRight?i:levelSize-1-i;
            levelNodes[index]=node->val;
            if(node->left!=NULL)
            {
                queue[rear++]=node->left;
            }
            if(node->right!=NULL)
            {
                queue[rear++]=node->right;
            }
        }
        (*returnSize)++;
        result=(int**)realloc(result,(*returnSize) * sizeof(int*));
        result[*returnSize - 1] = levelNodes;
        *returnColumnSizes=(int*)realloc(*returnColumnSizes,(*returnSize) * sizeof(int));
        (*returnColumnSizes)[*returnSize-1]=levelSize;
        leftToRight= !leftToRight;
    }
        free(queue);
        return result;
    
}