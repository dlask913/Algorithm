import java.util.ArrayList;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] A = new int[n][2];
        for(int i=0;i<n;i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            A[i][0] = x;
            A[i][1] = y;
        }
        int[] C = new int[n];
        int k = 0;
        while(k<n){
            int cnt = 1;
            for(int i = 0;i<n;i++){
                if(i==k) continue;
                if(A[k][0]<A[i][0] && A[k][1]<A[i][1]) cnt ++;
            }
            C[k] = cnt;
            k++;
        }
        for (int i =0;i<n;i++){
            System.out.print(C[i]+" ");
        }

    }
}