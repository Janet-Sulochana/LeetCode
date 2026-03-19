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
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue=new LinkedList<>();
        List<List<Integer>> result=new LinkedList<>();
        if(root==null) return result;
        queue.add(root);
        while(!queue.isEmpty()){
            int n=queue.size();
            List<Integer> temp=new LinkedList<>();
            for(int i=0;i<n;i++){
                TreeNode e=queue.poll();
                temp.add(e.val);
                if(e.left!=null) queue.add(e.left);
                if(e.right!=null) queue.add(e.right);
            }
            result.add(temp);
        }
        return result;
    }
}