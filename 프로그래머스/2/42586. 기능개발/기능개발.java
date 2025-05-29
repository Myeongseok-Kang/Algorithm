import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        /*
        bepo 에 배포 가능한 최소 날짜 저장
        bepo에 값 남아있다면 계속 반복
            v = bepo[0]
            bepo앞부분 탐색해서 v보다 작거나 같은것들 다 빼고 ans에 뺀 개수 넣음
        */
        ArrayList<Integer> ans = new ArrayList<>();
        int n = speeds.length;
        ArrayDeque<Integer> bepo = new ArrayDeque<>();
        for (int i = 0; i<n; i++){
            int remain = 100-progresses[i];
            int day = (remain%speeds[i] == 0? remain/speeds[i]: remain/speeds[i]+1);
            bepo.offerLast(day);
        }
        
        while (!bepo.isEmpty()){
            int v = bepo.peekFirst();
            int count = 0;
            while (!bepo.isEmpty() && bepo.peekFirst() <= v){
                count += 1;
                bepo.pollFirst();
            }
            ans.add(count);
        }
        int[] answer = ans.stream().mapToInt(i->i).toArray();
        return answer;
    }
}