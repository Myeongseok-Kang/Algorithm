import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i<numbers.length-1; i++){
            for (int j = i+1; j<numbers.length; j++){
                set.add(numbers[i]+numbers[j]);
            }
        }
        int[] ans = new int[set.size()];
        int i = 0;
        for (int x: set){
            ans[i++] = x;
        }
        Arrays.sort(ans);
        return ans;
    }
}