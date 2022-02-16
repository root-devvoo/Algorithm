class Solution {
    public String solution(String phone_number) {
        String answer = "";
        
        for (int i=0; i<phone_number.length(); i++) {
        	if (i<phone_number.length()-4) { // 별로 바꿔야될 부분
        		answer += '*';
        	} else {
        		answer += phone_number.charAt(i); // 숫자로 나타낼 부분
        	}
        }
        
        return answer;
    }
}
