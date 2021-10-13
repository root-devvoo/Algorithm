import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        int n;
        n = sc.nextInt();
        int[] arr = new int[n];

        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close(); // n에 지정한 수 만큼 반복해서 리스트에다 값을 넣고 close

        for(int i=1; i<n; i++) {
            // 타겟이 되는 인덱스의 넘버
            int target = arr[i];
            int j = i - 1;

            // 타겟이 이전 원소보다 크기 전까지 반복
            while(j >= 0 && target < arr[j]) {
                arr[j+1] = arr[j]; // 이전 원소를 한 칸씩 뒤로 미룬다
                j--;
            }
            arr[j+1] = target;
            /*
             * 위 반복문에서 탈출 하는 경우 앞의 원소가 타겟보다 작다는 의미이므로
             * 타겟 원소는 j번째 원소 뒤에 와야한다.
             * 그러므로 타겟은 j+1 에 위치하게 된다.
             */
        }

        for (int k=0; k<n; k++) {
            System.out.println(arr[k]);
        }
    }
}
