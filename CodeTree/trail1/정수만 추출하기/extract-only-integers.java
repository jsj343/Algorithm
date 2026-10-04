import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 두 개의 문자열 입력받기 (예: "123a45 789")
        String str1 = sc.next();
        String str2 = sc.next();
        
        // 각 문자열에서 숫자만 추출한 결과를 정수로 변환
        int num1 = extractInteger(str1);
        int num2 = extractInteger(str2);
        
        // 추출된 두 정수의 합 출력
        System.out.println(num1 + num2);
    }
    
    // 문자열에서 앞부분의 정수만 추출하는 메서드
    public static int extractInteger(String str) {
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            
            // Java 8 기준: 문자가 숫자인지 확인
            if (Character.isDigit(ch)) {
                sb.append(ch); // 숫자라면 추가
            } else {
                break; // 숫자가 아닌 문자를 만나면 즉시 중단
            }
        }
        
        // 누적된 문자열이 없다면 0 반환 (문제 조건에 따라 예외 처리 가능)
        if (sb.length() == 0) {
            return 0;
        }
        
        // 추출된 문자열을 정수(int)로 변환하여 반환
        return Integer.parseInt(sb.toString());
    }
}
