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

        // round는 배열 크기 - 1 만큼 진행됨
        for(int i=1; i<n; i++) {
            // 각 라운드별 비교횟수는 배열 크기의 현재 라운드를 뺀 만큼 비교한다
            for(int j=0; j < n-i; j++) {
                // 현재 원소가 다음 원소보다 클 경우 : 서로 원소의 위치를 교환한다
                if(arr[j] > arr[j+1]) {
                    // swap
                    swap(arr, j, j+1);
                }
            }
        }
        for (int k=0; k<n; k++) {
            System.out.println(arr[k]);
        }
    }
    //////////////////////////////////////////////////////////////////////////////////////////////////////
    // swap 해주는 기능 따로 지정
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
