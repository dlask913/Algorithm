import java.util.Random;
import java.util.Scanner;
public class ShortestPath {

    // 가중치 그래프 만들기
    private void Init(int[][] A){
        Random r = new Random();
        final int INF = Integer.MAX_VALUE;
        for(int i=0;i<A.length;i++){
            for(int j=0;j<A.length;j++){
                if(i==j) A[i][j]=0;
                else A[i][j]=A[j][i]=r.nextInt(10)+1;
            }
        }
        // 가중치그래프 출력
        System.out.println("------------------------");
        for(int i=0;i<A.length;i++){
            for(int j=0;j<A.length;j++){
                System.out.print(A[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println("------------------------");
    }

    private void Shortestpath(int[][] A,int[] D, int s,int q) {
        int n = 0,i=0;
        while (n <= q) { // 경유하기 전 연결되어있는 점들과의 거리 배열 D에 담아주기
            D[n] = A[s][n]; // = A[s][i] -> 여기서 s는 출발점 위치
            n++;
        }
        // index별로 최소거리 계속 갱신
        while(i<=q){
            Update(A, D, i);
            i++;
        }
    }
    // 갱신
    private void Update(int[][] A, int[] D,int idx){
        for(int i=0;i<D.length;i++){
            if ((i != 0) && (i != idx)){
                if((D[idx]+A[idx][i])<D[i]) D[i]=D[idx]+A[idx][i];
            }
        }
    }
    public static void main(String[] args) {
        final int INF = Integer.MAX_VALUE;
        Scanner scan = new Scanner(System.in);

        // size 입력받기 ( 점의 수 )
        int size = scan.nextInt();
        int[][]G = new int[size][size];
        ShortestPath sh = new ShortestPath();

        // 그래프 초기화
        sh.Init(G);

        int n = G.length; // 점의 수
        int[] D = new int[n]; // 입력받은 점을 기준으로 각 점들까지의 최소거리 저장하는 배열

        sh.Shortestpath(G,D,0,n-1);

        for ( int i =0;i<D.length;i++){
            System.out.println("0에서 "+i+"까지의 최소거리 ==> "+ D[i]);
        }
    }
}
