import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        int n = discount.length;
        HashMap<String,Integer> count;
        A: for (int i = 0; i<=n-10; i++){
            count = new HashMap<>();
            
            for (int j = i; j<10+i; j++){
                count.put(discount[j],count.getOrDefault(discount[j],0) + 1);
            }
            
            for (int j = 0; j<want.length; j++){
                if (number[j] != count.getOrDefault(want[j],0))
                    {
                    continue A;
                }
            }
            answer += 1;
        }
        
        return answer;
    }
}