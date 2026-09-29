import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int[] arr1 = new int[n1];
        int[] arr2 = new int[n2];
        for(int i=0; i<n1; i++)
            arr1[i] = sc.nextInt();
        for(int i=0; i<n2; i++)
            arr2[i] = sc.nextInt();

        String ans = "No";
        int idx = 0;
        
        for(int i=0; i<n1; i++){
            if(ans=="Yes")
              break;
            if(arr1[i]==arr2[idx]){
                idx += 1;
                for(int j=i+1; j<n1; j++){                                 
                    if(arr1[j] == arr2[idx]){
                        idx += 1;
                        if((idx+1)==n2){
                            ans = "Yes";
                            break;
                        }   
                    }                      
                    else{
                        idx = 0;
                        break;
                    }                        
                }
            }
            else
                continue;
        }
        System.out.print(ans);
    }
}