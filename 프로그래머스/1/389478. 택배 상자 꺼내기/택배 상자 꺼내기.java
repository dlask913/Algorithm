class Solution {
    public int solution(int n, int w, int num) {
        int answer = 1;
        
        /* 나머지로 규칙을 찾았을 때
        현 박스에서 바로 위 박스까지의 거리가 1, 2*w-1, 2*w-3, ..
        */
        int[] arr = new int[w];
        arr[0] = 1;
        for (int i=w-1; i>=1; i--){
            arr[w-i] = (i+1)*2-1;
        }
        
        // 현재 위치 currentPos 에서 위로 올라갈때마다 카운트하기
        int currentPos = num;
        while (true){
            int idx = currentPos % w;
            currentPos += arr[idx];
            if(currentPos > n) break;
            answer += 1;
        }
        
        return answer;
    }
}