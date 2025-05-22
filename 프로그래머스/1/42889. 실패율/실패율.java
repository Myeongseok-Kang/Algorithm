import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        
        if (N==1){return new int[]{1};}
        
        
        int[] stageCount = new int[N];
        int clear = 0;
        for (int n : stages){
            if (n == N+1) {
                clear += 1;
                continue;
            }
            stageCount[n-1] += 1;
        }
        
        int[] allCount = new int[N];
        allCount[N-1] = stageCount[N-1] + clear;
        for (int i = N-2; i>=0; i--){
            allCount[i] = allCount[i+1] + stageCount[i];
        }
        
        HashMap<Integer, Double> fail = new HashMap<>();
        
        for (int i = 0; i<N; i++){
            if (allCount[i] == 0){
                fail.put(i+1,0.);
            }
            else {
                fail.put(i+1,(double)stageCount[i]/allCount[i]);
            }
        }
        System.out.println(fail);
        
        List<Integer> list = new ArrayList<>(fail.keySet());
        list.sort((o1,o2)->Double.compare(fail.get(o2),fail.get(o1)));
        return list.stream().mapToInt(i->i).toArray();
        
    }
}