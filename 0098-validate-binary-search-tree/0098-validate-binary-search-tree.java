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
    public static boolean utility(TreeNode root,TreeNode s,TreeNode b){
        if(root==null)return true;
        if(s!=null && s.val <= root.val) return false;
        if(b!=null && b.val >= root.val) return false;
        return utility(root.left,root,b)&&utility(root.right,s,root);
    }
    public boolean isValidBST(TreeNode root) {
        TreeNode small=null;
        TreeNode big=null;
        boolean result = utility(root,small,big);
        return result;
    }
}