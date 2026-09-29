import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str1 = sc.next();
        String str2 = sc.next();
        int idx = -1;
        int len_str2 = str2.length();
        for(int i=0; i<str1.length()-len_str2+1; i++){
            idx = i;
            int cnt = 0;
            for(int j=0; j<len_str2; j++){
                if(str1.charAt(i+j) != str2.charAt(j)){
                    idx = -1;
                    cnt = 0;
                    break;
                }
                else
                    cnt++;
            }
            if(cnt == len_str2)
                break;
        }
        System.out.print(idx);
    }
}