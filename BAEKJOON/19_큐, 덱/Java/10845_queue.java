import java.util.Scanner;

public class Main {
	public static int[] queue;
	public static int size = 0;
	public static int front = 0;
	public static int back = 0;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int N = sc.nextInt();
		queue = new int[N];
		
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
				
			case "front":
				sb.append(front()).append('\n');
				break;
			
			case "back":
				sb.append(back()).append('\n');
				break;	
			}
		}
		System.out.println(sb);
	}

	private static void push(int item) {
		queue[back] = item;
		back++;
		size++;
	}
	
	private static int pop() {
		if (size == 0) {
			return -1;
		} else {
			int result = queue[front];
			queue[front] = 0;
			size--;
			front++;
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
	
	private static int front() {
		if (size == 0) {
			return -1;
		}
		else {
			return queue[front];
		}
	}

	private static int back() {
		if (size == 0) {
			return -1;
		}
		else {
			return queue[back - 1];
		}
	}
}
