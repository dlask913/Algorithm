import java.util.Arrays;
import java.util.Comparator;
import java.util.Random;

public class ClosetPair {

    private void merge (int[][] A, int[][] D, int p, int k, int q ){
        double d = 0;
        int[][] CP_L = new int[2][2];
        int[][] CP_R = new int[2][2];
        int[][] CP_C = new int[2][2];
        double l = dist(A,CP_L,p,k);
        double r = dist(A,CP_R,k+1,q);

        // 조건 : l 과 r 중에 짧은 거리를 d라고 놓는다.
        if (l<= r) d = l;
        else d = r;

        for(int i = 0; i<A.length;i++) {
            if ((A[k][0] - d) <= A[i][0]) {
                p = i;
                break;
            }
        }
        for(int i = A.length-1; i>=0;i--) {
            if ((A[k+1][0] + d) >= A[i][0]) {
                q = i;
                break;
            }
        }
        double c=dist (A,CP_C,p,q);
        if ((l <= r) && (l <= c )) {
            for (int i=0;i<2;i++){
                D[i][0]=CP_L[i][0];
                D[i][1]=CP_L[i][1];
            }
        }
        else if ((r <= l) && (r <=c)){
            for (int i=0;i<2;i++){
                D[i][0]=CP_R[i][0];
                D[i][1]=CP_R[i][1];
            }
        }
        else if ((c <= l) && (c <=r)){
            for (int i=0;i<2;i++){
                D[i][0]=CP_C[i][0];
                D[i][1]=CP_C[i][1];
            }
        }
    }

    // 거리 구하기
    private double dist(int[][] A, int[][] D, int p, int q){
        double min=0;
        int n=0;
        for ( int a = p; a< q; a++) {
            double x = Math.pow(A[a][0] - A[a + 1][0], 2);
            double y = Math.pow(A[a][1] - A[a + 1][1], 2);
            double d = Math.sqrt(x + y);
            if (a == p || d < min) {
                min = d;
                n = a;
            }
        }
        for (int i = 0; i < 2; i++) {
            D[i][0] = A[n][0];
            D[i][1] = A[n][1];
            n++;
        }
        return min;
    }

    // 분할
    private void ClosestPair(int[][] A,int[][] D, int p, int q) {
        if(q-p<=3) return;
        int k = (p+q)/2;
        ClosestPair(A,D, p, k); // - > CP_L ( 왼쪽 재귀 호출 )
        ClosestPair(A,D,k+1, q); // -> CP_R ( 오른쪽 재귀 호출 )
        merge(A, D, p, k, q);
    }

    public static void main(String[] args) {
        Random r = new Random();
        int[][] S = new int[10][2]; /* (x,y)에 있는 10개의 점을 담을 배열 선언
                                       -  [i][0] -> x좌표 , [i][1] -> y좌표
                                       -  점들의 개수를 N개로 가정할 경우 N > 4        */
        int[][] D = new int[2][2]; // 최근접 점 쌍을 담을 배열 선언 ( 쌍이므로 점의 개수를 2로 가정 )

        // ( x, y ) 에 각각 0~ 9 숫자를 랜덤 저장
        for (int i = 0; i < S.length; i++) {
            for (int j = 0; j < S[i].length; j++) {
                S[i][j] = r.nextInt(10);
            }
        }
        // x좌표 기준 오름차순으로 정렬
        Arrays.sort(S, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if(o1[0] == o2[0]) return o1[1] -o2[1];
                else return o1[0] -o2[0];
            }
        });
        // 점들의 좌표(위치) 출력
        for (int[] ints : S) {
            System.out.printf("( %d , %d )", ints[0], ints[1]);
            System.out.println();
        }
        ClosetPair closet = new ClosetPair();
        closet.ClosestPair(S, D, 0, S.length-1);
        // 모든 실행 후 최근접 점 쌍 출력
        System.out.print("최근접 점 쌍 : ");
        for (int i=0;i<2;i++) System.out.print("( " + D[i][0]+","+D[i][1] +" )"  );
        System.out.println();
    }
}