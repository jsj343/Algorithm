import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[2][4];
        for(int i=0; i<2; i++){
            for(int j=0; j<4; j++)
                arr[i][j] = sc.nextInt();
        }
        double row1=0, row2=0, col1=0, col2=0, col3=0, col4=0, total=0;
        for(int i=0; i<2; i++){
            for(int j=0; j<4; j++)
                total += arr[i][j];
        }
        for(int i=0; i<2; i++){
            col1 += arr[i][0];
            col2 += arr[i][1];
            col3 += arr[i][2];
            col4 += arr[i][3]; 
        }
            
        for(int j=0; j<4; j++){
            row1 += arr[0][j];
            row2 += arr[1][j]; 
        }
        System.out.printf("%.1f %.1f\n", row1/4, row2/4);
        System.out.printf("%.1f %.1f %.1f %.1f\n", col1/2,col2/2,col3/2,col4/2);
        System.out.printf("%.1f", total/8);
    }
}