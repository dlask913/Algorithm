class Solution {
    public int solution(int[][] signals) {
        int n = signals.length;
        int[] periods = new int[n];
        
        int maxTime = 1;
        for(int i=0; i<n; i++){
            periods[i] = signals[i][0] + signals[i][1] + signals[i][2];
            maxTime = getLCM(maxTime, periods[i]);
        }

        for(int t=1; t<maxTime; t++){
            boolean yellowFlag = true;
            
            for (int i=0; i<n; i++){
                int green = signals[i][0];
                int yellow = signals[i][1];
                int period = periods[i];
                
                // 현재 시간 t에서 주기로 나눈 위치
                int currentPos = t % period;
                if (currentPos == 0) currentPos = period;
                
                if (currentPos <= green || currentPos > green + yellow) {
                    yellowFlag = false;
                    break;
                }
            }
            
            if (yellowFlag) {
                return t;
            }
        }
            
        return -1;
    }
    
    // 유클리드 호제법을 이용한 최대공약수 구하기
    public int getGCD(int a, int b){
        while (b!=0){
            int r = a % b;
            a = b;
            b = r; 
        }
        return a;
    }
    
    // 공식을 이용한 최소공배수 구하기
    public int getLCM(int a, int b){
        return (a * b) / getGCD(a, b);
    }
}