import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        char[] lst = S.toCharArray();
        int Q = sc.nextInt();
        for(int i=0; i<Q; i++){
            int quest = sc.nextInt();
            if(quest == 1){
                int a = sc.nextInt();
                int b = sc.nextInt();
                char temp1 = lst[a-1];
                char temp2 = lst[b-1];
                lst[a-1] = temp2;
                lst[b-1] = temp1;
                String ans = new String(lst);
                System.out.println(ans);
                // char char1 = S.charAt(b-1);
                // char char2 = S.charAt(a-1);
                // String ans = S.substring(0,a-1) + char1 + S.substring(a-1,b-1) + char2 + S.substring(b-1);       
                
                // System.out.println(ans);
            }
            else if(quest == 2){
                char x = sc.next().charAt(0);
                char y = sc.next().charAt(0);
                for(int j=0; j<lst.length; j++){
                    if(lst[j]==x)
                        lst[j] = y;
                }
                String ans = new String(lst);
                System.out.println(ans);                    
            }
        }
    }
}