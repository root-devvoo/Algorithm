class Solution {
    public boolean solution(int x) throws Exception {
        int sum = 0;
        int x2 = x;
        
        while (x2 >= 1) {
            sum += x2%10;
            x2 /= 10;
        }
        
        if (x % sum == 0) {
            return true;
        
        } else {
            return false;
        }     
    }
}
