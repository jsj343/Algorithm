import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        int idx = -1;

        for(int i=0; i<N; i++){
            arr[i] = sc.nextInt();
        }
        int endpoint = N;
        while(idx != 0){
            int INT_MAX = Integer.MIN_VALUE;
            // 1. 가장 왼쪽에 있는 최댓값의 위치 찾기
            for(int i=0; i<endpoint; i++){
                if(arr[i]>INT_MAX){
                    INT_MAX = arr[i];
                    idx = i;
                }
            }
            System.out.print(idx+1+" ");
            endpoint = idx; 
        }
    }
}