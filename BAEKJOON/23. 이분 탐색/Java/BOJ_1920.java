import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

// hash set을 이용한 풀이
public class BOJ_1920 { // public class Main
    public static void main(String[] args) {
        // input
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        Set<Integer> A = new HashSet<>(); // 알고 있는 그 set임
        for (int i = 0; i < N; i++) {
            int n = scanner.nextInt();
            A.add(n);
        }

        StringBuilder result = new StringBuilder();

        int M = scanner.nextInt();
        for (int i = 0; i < M; i++) {
            int m = scanner.nextInt();

            // 이 for문 돌면서 set 안에 존재하는지 아닌지 판별
            if (A.contains(m)) {
                result.append(1 + "\n");
            } else {
                result.append(0 + "\n");
            }
        }
        System.out.println(result.toString());
    }
}
