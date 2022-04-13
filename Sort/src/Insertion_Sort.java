import java.util.Random;
import java.util.Scanner;


public class Insertion_Sort {
    // 값 저장 & 중복 제거
    private void input(int[] A){
        Random r = new Random();
        for (int i=0;i<A.length;i++){
            A[i]=r.nextInt(10000)+1;
            if(i != 0){
                int j = 0;
                while(j<i) {
                    if(A[j++] ==A[i]) i --;
                }
            }
        }
        for (int k : A) System.out.print(k + ", ");
        System.out.println();
    }

    private int[] Insertion(int[] A){
        int current = 0;
        int a = 0;
        for ( int i = 1; i<A.length;i++){
            current = A[i];
            int j = i-1;
            while ( j>=0 && A[j]>current){
                a = A[j+1];
                A[j+1] = A[j];
                A[j]=a;
                j = j-1;
            }
        }
        return A;
    }

    public static void main(String[] args){

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] A = new int[n];
        Insertion_Sort insertion = new Insertion_Sort();
        insertion.input(A);
        insertion.Insertion(A);
        for (int k : A) System.out.print(k + ", ");

    }

}
