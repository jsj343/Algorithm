import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[][] arr = new int[N][M];
        int num = 1;

        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(arr[i][j]==0){
                    arr[i][j] = num++;
                    int r = i+1;
                    int c = j-1;
                    while(in_range(r,c, N, M)){
                        arr[r][c] = num++;
                        r++;
                        c--;
                    }
                }
            }
        }

        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }    
    }

    public static boolean in_range(int row, int col, int N, int M){
            return (row>=0) && (row<N) && (col>=0) && (col<M); 
    }
}