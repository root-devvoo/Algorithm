import java.util.Scanner;

public class Main {
	public static int[] stack;
	public static int size = 0;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int N = sc.nextInt();
		stack = new int[N];
		
		for (int i=0; i<N; i++) {
			String command = sc.next();
			
			switch (command) {
			case "push":
				push(sc.nextInt());
				break;
			
			case "pop":	
				sb.append(pop()).append('\n');
				break;
			
			case "size":
				sb.append(size()).append('\n');
				break;
			
			case "empty":
				sb.append(empty()).append('\n');
				break;
				
			case "top":
				sb.append(top()).append('\n');
				break;
			}
		}
		System.out.println(sb);
	}
	private static void push(int item) {
		stack[size] = item;
		size++;
	}
	
	private static int pop() {
		if (size == 0) {
			return -1;
		} else {
			int result = stack[size - 1];
			stack[size - 1] = 0;
			size--;
			return result;
		}	
	}
	
	private static int size() {
		return size;
	}
	
	private static int empty() {
		if (size == 0) {
			return 1;
		} else {
			return 0;
		}
	}
	
	private static Object top() {
		if (size == 0) {
			return -1;
		} else {
			return stack[size - 1];
		}
	}
}
