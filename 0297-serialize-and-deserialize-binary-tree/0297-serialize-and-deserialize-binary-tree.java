/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
    
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if(root==null) return "";
        StringBuilder str=new StringBuilder();
        Queue<TreeNode> queue=new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()){
            TreeNode temp=queue.poll();
            if(temp==null){
                str.append("null,");
                continue;
            }
            str.append(temp.val).append(",");
            queue.add(temp.left);
            queue.add(temp.right);
           
        }
         return str.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if(data==null||data.isEmpty()) return null;
        String a[]=data.split(",");
        TreeNode root=new TreeNode(Integer.parseInt(a[0]));
        Queue<TreeNode> queue=new LinkedList<>();
        queue.add(root);
        int i=1;
        while(!queue.isEmpty()){
            TreeNode par=queue.poll();
            if(!a[i].equals("null")){
                par.left=new TreeNode(Integer.parseInt(a[i]));
                queue.add(par.left);
            }
            i++;
            if(!a[i].equals("null")){
                par.right=new TreeNode(Integer.parseInt(a[i]));
                queue.add(par.right);
            }
            i++;
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));