class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int idx = 0;
        while(idx < section.length) {
            int cur = section[idx];
            int s = idx;
            for (int i = s; i<section.length; i++){
                n = section[i];
                if(n >= cur+m) break;
                idx = i+1;
            }
            answer++;
        }
        return answer;
    }
}