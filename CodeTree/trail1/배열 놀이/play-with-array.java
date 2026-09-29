import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int Q = sc.nextInt();
        int[] arr = new int[N];
        for(int i=0; i<N; i++) 
            arr[i] = sc.nextInt();
        for(int i=0; i<Q; i++){
            int question = sc.nextInt();
            if(question==1){
                int a = sc.nextInt();
                System.out.println(arr[a-1]);
            }
            else if(question==2){
                int b = sc.nextInt();
                int idx = 0;
                boolean flag = false;
                for(int j=0; j<N; j++){
                    if(arr[j]==b){
                        flag = true;
                        break;
                    }
                    else
                        idx++;
                }
                if(flag)
                    System.out.println(idx+1);
                else
                    System.out.println(0);                
            }
            else if(question==3){
                int s = sc.nextInt();
                int e = sc.nextInt();
                for(int j=s-1; j<e; j++)
                    System.out.print(arr[j]+" ");
                System.out.println();
            }
        }
    }
}