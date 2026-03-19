/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int maxPS=Integer.MIN_VALUE;
    public int DFS(TreeNode root){
        if(root==null)return 0;
        int Left=Math.max(0,DFS(root.left));
        int Right=Math.max(0,DFS(root.right));
        int curSum=Left+Right+root.val;
        maxPS=Math.max(curSum,maxPS);
        return root.val + Math.max(Left,Right);
    }
    public int maxPathSum(TreeNode root) {
        DFS(root);
        return maxPS; 
    }
}