import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        /*
        12345 (5)
        212 324 25 (8)
        33 11 22 44 55 (10)
        
        정답맞춘개수배열
        정답맞춘개수세기 :
            answer 인덱스 :
                
        */
        int[] c1 = {1,2,3,4,5};
        int[] c2 = {2,1,2,3,2,4,2,5};
        int[] c3 = {3,3,1,1,2,2,4,4,5,5};
        int[] check = new int[3];
        for (int i = 0; i<answers.length; i++){
            if (answers[i] == c1[i%5]){
                check[0] += 1;
            }
            if (answers[i] == c2[i%8]){
                check[1] += 1;
            }
            if (answers[i] == c3[i%10]){
                check[2] += 1;
            }
        }
        int maxVal = check[0];
        for (int i = 1; i<3; i++){
            maxVal = Math.max(check[i],maxVal);
        }
        ArrayList<Integer> ar = new ArrayList<>();
        for (int i = 0; i<3; i++){
            if (check[i] == maxVal){
                ar.add(i+1);
            }
        }
        int i = 0;
        int[] ans = new int[ar.size()];
        for (int x: ar){
            ans[i++] = x;
        }
        return ans;
    }
}