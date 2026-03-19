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
    public int minDepth(TreeNode root) {
        int result=0;
        if(root==null) return 0;
        if(root.left==null){
            result= 1 + minDepth(root.right);
        }
        if(root.right==null){
            result= 1 + minDepth(root.left);
        }
        if(root.left!=null && root.right!=null){
            result= 1 + Math.min(minDepth(root.left),minDepth(root.right));
        }
        return result;
    }
}