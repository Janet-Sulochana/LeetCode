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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result=new LinkedList<>();
        if(root==null)return result;
        Queue<TreeNode> queue=new LinkedList<>();
        queue.add(root);
        boolean flag=true;
        while(!queue.isEmpty()){
            int n=queue.size();
            List<Integer> temp=new LinkedList<>();
            for(int i=0;i<n;i++){
                TreeNode node=queue.poll();
                if(flag){
                    temp.addLast(node.val);
                }
                else{
                    temp.addFirst(node.val);
                }
                if(node.left!=null){
                    queue.add(node.left);
                }
                if(node.right!=null){
                    queue.add(node.right);
                }
                
            }
            flag=!flag;
            result.add(temp);

        }
        return result;
    }
}