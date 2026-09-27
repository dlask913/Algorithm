import java.util.*;

class Node {
    List<Integer> candidates;
    int sheep;
    int wolf;
    
    Node (List<Integer> candidates, int sheep, int wolf){
        this.candidates = candidates;
        this.sheep = sheep;
        this.wolf = wolf;
    }
    
    void print(){
        System.out.printf("sheep: %d, wolf: %d \n", sheep, wolf);
    }
}

class Solution {    
    public int solution(int[] info, int[][] edges) {
        int answer = 1;
        int n = info.length;
        HashMap<Integer, List<Integer>> leafMap = new HashMap<>();
        Deque<Node> dq = new ArrayDeque<>();
        
        // 1. 노드별 자식 노드 정리
        for(int i=0; i<n; i++){
            leafMap.put(i, new ArrayList<>());
        }
        for(int i=0; i<edges.length; i++){
            leafMap.get(edges[i][0]).add(edges[i][1]);
        }
        
        // 첫번째 노드 (양 0, 늑대 1)
        dq.add(new Node(new ArrayList<>(leafMap.get(0)), 1, 0));
        
        // 2. 다음 탐색할 후보군들을 업데이트 하며 bfs
        while(!dq.isEmpty()){
            Node current = dq.poll();
            answer = Math.max(answer, current.sheep);
           
            for(int next : current.candidates){
                int sheep = current.sheep;
                int wolf = current.wolf;
                
                if(info[next]==0) sheep++;
                else wolf++;
                
                if(wolf>=sheep) continue;
                
                // 기존 후보를 유지하면서 새 목록 만들기
                List<Integer> nextCandidates = new ArrayList<>(current.candidates);
                
                // 기존 후보 - 다음 선택할 노드 + 다음 선택할 노드의 후보
                nextCandidates.remove(Integer.valueOf(next));
                nextCandidates.addAll(leafMap.get(next));
                
                dq.add(new Node(nextCandidates, sheep, wolf));                
            }
            
        }
        
        return answer;
    }
}