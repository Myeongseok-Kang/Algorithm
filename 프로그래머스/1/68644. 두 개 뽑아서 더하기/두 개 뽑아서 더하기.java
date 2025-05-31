import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        ArrayList<Integer> list = new ArrayList<>();
        int n = numbers.length;
        /*
        i j로 모든 조합 탐색하면서 더한 값 list에 넣음
        list 에서 중복 제거하고 정렬해서 배열로 리턴
        */
        for (int i = 0; i<n-1; i++){
            for (int j = i+1; j<n; j++){
                list.add(numbers[i]+numbers[j]);
            }
        }
        int[] answer = list.stream().distinct().mapToInt(i->i).toArray();
        Arrays.sort(answer);
        
        return answer;
    }
}