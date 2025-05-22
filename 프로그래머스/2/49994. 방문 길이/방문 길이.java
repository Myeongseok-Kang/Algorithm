import java.util.*;

class Solution {
    private static boolean isCanMove(int nx, int ny){
        if (nx < 0 || nx > 10) {return false;}
        if (ny < 0 || ny > 10) {return false;}
        return true;
    }
    
    private static final HashMap<Character,int[]> move = new HashMap<>();
    static{
    move.put('U',new int[]{0,1});
    move.put('D',new int[]{0,-1});
    move.put('L',new int[]{-1,0});
    move.put('R',new int[]{1,0});
    }
    
    private static final HashSet<String> check = new HashSet<>();
    
    public int solution(String dirs) {
        int answer = 0;
        int x = 5, y = 5;
        HashSet<String> ans = new HashSet<>();
        
        for (char c: dirs.toCharArray()){
            int[] moveD = move.get(c);
            int nx = moveD[0] + x, ny = moveD[1] + y;
            if (!isCanMove(nx,ny)) {continue;}
            check.add(nx+" "+ny+" "+x+" "+y);
            check.add(x+" "+y+" "+nx+" "+ny);
            x = nx;
            y = ny;
        }
        
        return check.size()/2;
        
        /*
        길 하나씩
            움직일 수 없으면
                continue
            움직일 수 있으면
                움직인다
                만약 움직인 곳이 새로우면 ans +1
        */
        
        /*
        
        
        */
    }
}