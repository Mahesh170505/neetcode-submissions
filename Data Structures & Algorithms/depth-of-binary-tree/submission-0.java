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
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> elementQ = new LinkedList<>();
        int levelCount = 0;
        elementQ.add(root);


        while(!elementQ.isEmpty()){
            int nodeCount = elementQ.size();
            
            while(nodeCount > 0){
                TreeNode element = elementQ.poll();
                if(element.left != null){
                    elementQ.add(element.left);
                }
                 if(element.right != null){
                    elementQ.add(element.right);
                }
                nodeCount--;
            }
            levelCount++;
        }
        return levelCount;
    }
}
