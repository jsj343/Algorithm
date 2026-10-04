import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int number = sc.nextInt();
        String ans = "";

        for(int i=0; i<number; i++){
            int quest = sc.nextInt();
            switch(quest){
                case 1:
                    ans = str.substring(1, str.length()) + str.substring(0, 1);
                    str = ans;
                    break;
                case 2:
                    ans = str.substring(str.length()-1, str.length()) + str.substring(0, str.length()-1);
                    str = ans;
                    break;
                case 3:
                    ans = new StringBuilder(str).reverse().toString();
                    str = ans;
                    break;
            }
            System.out.println(ans);
        }
    }
}