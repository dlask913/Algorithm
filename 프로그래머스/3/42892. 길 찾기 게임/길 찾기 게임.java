import java.util.*;

class Node{
    int x, y, num;
    Node left, right;
    
    Node(int num, int x, int y){
        this.num = num;
        this.x = x;
        this.y = y;
    }
    
    void print(){
        System.out.printf("num: %d, x: %d, y: %d\n", num, x, y);
    }
}

class Solution {
    HashMap<Integer, List<Node>> nodeMap = new HashMap<>();
    public int[][] solution(int[][] nodeinfo) {
        int[][] answer = new int[2][];
        int n = nodeinfo.length;
        Node[] nodes = new Node[n];
        for (int i=0; i<n; i++){
            nodes[i] = new Node(i+1, nodeinfo[i][0], nodeinfo[i][1]);
        }
        
        Arrays.sort(nodes, (o1, o2) -> {
            if(o1.y == o2.y) // level 이 같으면 x 기준 오름차순
                return Integer.compare(o1.x, o2.x); 
            return Integer.compare(o2.y, o1.y);
        });
        
        Node root = nodes[0];
        
        for(int i=1; i<n; i++){
            Node parent = root; 
            while (true){
                if(nodes[i].x < parent.x){ // 부모 노드의 왼쪽인 경우
                    if(parent.left == null) {
                        parent.left = nodes[i];
                        break;
                    } else {
                        parent = parent.left;
                    }
                } else { // 부모 노드의 오른쪽인 경우 
                    if(parent.right == null){
                        parent.right = nodes[i];
                        break;
                    } else {
                        parent = parent.right; 
                    }
                }
            }
        }
        
        List<Integer> preList = new ArrayList<>();
        preOrder(root, preList);
        
        List<Integer> postList = new ArrayList<>();
        postOrder(root, postList);
        
        answer[0] = preList.stream().mapToInt(Integer::intValue).toArray();
        answer[1] = postList.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
    
    void preOrder(Node node, List<Integer> preList){
        preList.add(node.num);
        if(node.left != null) preOrder(node.left, preList);
        if(node.right != null) preOrder(node.right, preList);
    }
    
    void postOrder(Node node, List<Integer> postList){
        if(node.left != null) postOrder(node.left, postList);
        if(node.right != null) postOrder(node.right, postList);
        postList.add(node.num);
    }
}