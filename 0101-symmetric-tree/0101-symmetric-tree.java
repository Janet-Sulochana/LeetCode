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
    public static boolean utility(TreeNode l,TreeNode r){
        if(l==null && r==null)return true;
        if(l==null || r==null)return false;
        return l.val==r.val && utility(l.left,r.right) && utility(l.right,r.left);
    }
    public boolean isSymmetric(TreeNode root) {
        boolean result=utility(root.left,root.right);
        return result;
    }
}