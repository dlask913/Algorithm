import java.util.ArrayList;
import java.util.Random;
import java.util.TreeSet;

public class JobScheduling {

    private static void greedy(int[] L, int n, int m) {
        int[] M = new int[m];
        int max  = 0; // 종료시간
        int idx = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0) M[i] = L[i];
            else {
                int min = Integer.MAX_VALUE;
                for (int j = 0; j < m; j++) {
                    if (min > M[j]) {
                        min = M[j];
                        idx = j;
                    }
                }
                M[idx] = M[idx] + L[i];
                for (int j = 0; j < m; j++) {
                    if (max < M[j])  max = M[j];
                }
            }
        }
        System.out.println(max);
    }
    private static void Bruteforce(int[] L, int n, int m) {
        int[] M = new int[m];
        int max = 0;
        int idx = 0;
        ArrayList<Integer> A = new ArrayList<>();

        // 기계 하나에 다 들어갔을 때  0:4 , 0:8, 0:16
        for(int i = 0; i<n; i++){
            max += L[i];
        }
        A.add(max);
        // 1:3 , 1:7 , 1:15
        for ( int i =0; i<n; i++){
            max = 0;
            for(int j = 0; j<n; j++){
                if(i!=j) max += L[j];
            }
            if(max<L[i]) max = L[i];
            A.add(max);
        }
        // 2:2 , 2:6 , 2:14
        for(int i = 0; i<n;i++){
            for(int j =0; j<n;j++){
                max = 0;
                if(i != j){
                    max = L[i]+L[j];
                    int x = 0;
                    for ( int k =0; k<n; k++){
                        if(i!=k && j!=k) x += L[k];
                    }
                    if (max<x) max = x;
                    A.add(max);
                }
            }
        }
        // 3:5, 3:13
        for(int i =0;i<n;i++){
            for ( int j =0; j<n;j++){
                for(int k = 0; k<n;k++){
                    if(i != j && j != k && i != k){
                        max = L[i]+L[j]+L[k];
                        int x = 0;
                        for( int l = 0; l<n ; l++){
                            if(l!=i && l!=j && l!=k) x += L[l];
                        }
                        if(max<x) max = x;
                        A.add(max);
                    }
                }
            }
        }
        // 4:4 , 8:8
        for(int i = 0; i<(2/n); i++){
            int x = 0;
            max = 0;
            for ( int j = i; j<(i+(2/n)); j++){
                max += L[j];
                for ( int k = 0; k<n; k++){
                    if(k != j) x += L[k];
                }
            }
            if(max<x) max = x;
            A.add(max);
        }
        // 4:4, 4:12
        for(int i =0;i<n;i++){
            for ( int j =0; j<n;j++){
                for(int k = 0; k<n;k++){
                    for(int s = 0; s<n; s++) {
                        if (i != j && j != k && i != k && i != s && j!=s && k!=s) {
                            max = L[i] + L[j] + L[k]+L[s];
                            int x = 0;
                            for (int l = 0; l < n; l++) {
                                if (l != i && l != j && l != k && l!=s) x += L[l];
                            }
                            if (max < x) max = x;
                            A.add(max);
                        }
                    }
                }
            }
        }
        // 5: 11
        for(int i =0;i<n;i++){
            for ( int j =0; j<n;j++){
                for(int k = 0; k<n;k++){
                    for(int s = 0; s<n; s++) {
                        for ( int q = 0; q<n ; q++) {
                            if (i != j && j != k && i != k && i != s && j != s
                                    && k != s && q!=i && q!=j && q!=k && q!=s) {
                                max = L[i] + L[j] + L[k] + L[s] + L[q];
                                int x = 0;
                                for (int l = 0; l < n; l++) {
                                    if (l != i && l != j && l != k && l != s && l!=q) x += L[l];
                                }
                                if (max < x) max = x;
                                A.add(max);
                            }
                        }
                    }
                }
            }
        }
        // 6:10
        for(int i =0;i<n;i++){
            for ( int j =0; j<n;j++){
                for(int k = 0; k<n;k++){
                    for(int s = 0; s<n; s++) {
                        for ( int q = 0; q<n ; q++) {
                            for(int r = 0; r<n; r++) {
                                if (i != j && j != k && i != k && i != s && j != s
                                        && k != s && q != i && q != j && q != k
                                        && q != s && r != i && r!=j && r!= k && r!=s && r!=q) {
                                    max = L[i] + L[j] + L[k] + L[s] + L[q]+L[r];
                                    int x = 0;
                                    for (int l = 0; l < n; l++) {
                                        if (l != i && l != j && l != k && l != s && l != q && l!=r) x += L[l];
                                    }
                                    if (max < x) max = x;
                                    A.add(max);
                                }
                            }
                        }
                    }
                }
            }
        }
        // 7:9
        for(int i =0;i<n;i++){
            for ( int j =0; j<n;j++){
                for(int k = 0; k<n;k++){
                    for(int s = 0; s<n; s++) {
                        for ( int q = 0; q<n ; q++) {
                            for(int r = 0; r<n; r++) {
                                for (int t = 0; t<n ; t++) {
                                    if (i != j && j != k && i != k && i != s && j != s
                                            && k != s && q != i && q != j && q != k
                                            && q != s && r != i && r != j && r != k && r != s
                                            && r != q && t!=i && t!=j && t!=k && t!=s && t!=q && t!=r) {
                                        max = L[i] + L[j] + L[k] + L[s] + L[q] + L[r]+L[t];
                                        int x = 0;
                                        for (int l = 0; l < n; l++) {
                                            if (l != i && l != j && l != k && l != s
                                                    && l != q && l != r && l!=t) x += L[l];
                                        }
                                        if (max < x) max = x;
                                        A.add(max);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        TreeSet<Integer> Sort = new TreeSet<Integer>(A); // 중복 제거 및 정렬
        System.out.println(Sort.first());
    }

    public static void main(String[] args) {
        Random r = new Random();
        int[] n = new int[]{4,8,16};
        int m = 2;
        for(int i = 0; i<n.length;i++) {
            int[] L = new int[n[i]];
            for (int j = 0; j < L.length; j++) L[j] = r.nextInt(10)+1;
            System.out.print("할당해야하는 작업시간 : [ ");
            for (int j : L) System.out.print(j + " ");
            System.out.println("]");
            System.out.print("작업의 수가 " + n[i]+"일 때의 근사해 : ");
            greedy(L, n[i], m);
            System.out.print("작업의 수가 " + n[i]+"일 때의 최적해 : ");
            Bruteforce(L,n[i],m);
        }
    }
}
