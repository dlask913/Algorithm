class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        /*
        행렬 A의 크기: m*n, 행렬 B의 크기: n*p, 곱한 C의 크기: m*p
        */
        int m = arr1.length;
        int n = arr1[0].length;
        int p = arr2[0].length;
        int[][] answer = new int[m][p];
        for(int i=0; i<m; i++){
            for(int j=0; j<p; j++){
                for(int k=0; k<n; k++){
                    answer[i][j] += arr1[i][k]*arr2[k][j];
                }
            }
        }
        return answer;
    }
}