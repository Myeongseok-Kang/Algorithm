import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] ans = new int[prices.length];

        Deque<int[]> stack = new ArrayDeque<>();
        for (int i = 0; i<prices.length; i++){
            int v = prices[i];
            if (stack.isEmpty()){
                stack.push(new int[]{i,v});
            }
            else{
                while (!stack.isEmpty() && stack.peek()[1] > v){
                    int[] deleted = stack.pop();
                    ans[deleted[0]] = i - deleted[0];
                }
                stack.push(new int[]{i,v});
            }
        }
        while (!stack.isEmpty()){
            int[] pk = stack.pop();
            int i = pk[0];
            int v = pk[1];
            ans[i] = prices.length - 1 - i;
        }
        
        return ans;
    }
}