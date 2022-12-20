// 백준 11728번: 배열 합치기 (정렬, 두 포인터)
// 문제 URL: https://www.acmicpc.net/problem/11728

package list; // 백준에 제출할 때는 이 부분 지워야 됨

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BOJ_11728 { // 백준에 제출할 때 이 부분 public class Main으로 바꿔야 함

    public static void main(String[] args) {
        // input
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt(); // 배열 A의 사이즈
        int M = scanner.nextInt(); // 배열 B의 사이즈

        List<Integer> A = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int n = scanner.nextInt();
            A.add(n);
        }

        List<Integer> B = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            int n = scanner.nextInt();
            B.add(n);
        }
// TEST CODE
//        A.forEach(e -> System.out.println(e + " "));
//        B.forEach(e -> System.out.println(e + " "));

        // logic
        List<Integer> result = new ArrayList<>();

        int i = 0, j = 0; // 배열 A의 인덱스, 배열 B의 인덱스
        while (i < N && j < M) {
            int a = A.get(i);
            int b = B.get(j);

            if (a <= b) {
                result.add(a);
                i++;
            } else {
                result.add(b);
                j++;
            }
        }
        // 어느 한 배열의 사이즈가 여전히 남아있을 수 있으니까
        for (; i < N; i++) {
            result.add(A.get(i));
        }

        for (; j < M; j++) {
            result.add(B.get(j));
        }

        // output
        StringBuilder sb = new StringBuilder();
        for (int e : result) {
            sb.append(e + " ");
        }
        System.out.println(sb.toString());
    }
}
