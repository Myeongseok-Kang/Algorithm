import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "";
        int idx1 = 0;
        int idx2 = 0;
        for (String word: goal){
            if (idx1 < cards1.length && cards1[idx1].equals(word)){
                idx1 += 1;
                continue;
            }
            if (idx2 < cards2.length && cards2[idx2].equals(word)){
                idx2 += 1;
                continue;
            }
            return "No";
        }
        return "Yes";
    }
    
    
}