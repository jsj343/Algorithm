import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        List<Integer> arr = new ArrayList<>();
        for(int i=0; i<N; i++)
            arr.add(sc.nextInt());
        arr.sort(Comparator.reverseOrder());
        System.out.print(arr.get(0)+" "+arr.get(1));
    }
}