// package list;

import java.util.Scanner;

public class BOJ_3003 { // public class Main
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] chess = {1, 1, 2, 2, 2, 8};
        int[] pieces = new int[6];

        // list 안에 입력받은 숫자 넣고, 결과 출력
        for (int i=0; i<pieces.length; i++) {
            pieces[i] = sc.nextInt();
            System.out.print(chess[i]-pieces[i] + " ");
        }
    }
}
