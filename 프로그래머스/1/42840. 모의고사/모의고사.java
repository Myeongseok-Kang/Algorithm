import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] ans = new int[3];
        
        //1번  1, 2, 3, 4, 5
        //2번  2, 1, 2, 3, 2, 4, 2, 5
        //3번  3, 3, 1, 1, 2, 2, 4, 4, 5, 5
        
        int[][] pattern = {{1, 2, 3, 4, 5},{2, 1, 2, 3, 2, 4, 2, 5},{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        
        for (int i = 0; i<3; i++){
            for (int j = 0; j<answers.length; j++){
                if (pattern[i][j%pattern[i].length] == answers[j]){
                    ans[i] += 1;
                }
            }
        }
        int max = Arrays.stream(ans).max().getAsInt();
        ArrayList<Integer> fAns = new ArrayList<>();
        for (int i = 1; i<4; i++){
            if (max == ans[i-1]){
                fAns.add(i);
            }
        }
        return fAns.stream().mapToInt(i->i).toArray();
    }
}