import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int ans = 0;
        int n = board.length;
        ArrayList<Integer> dolls = new ArrayList<>();
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int m: moves){
            m -= 1;
            for (int y = 0; y < n; y++){
                if (board[y][m] != 0){
                    dolls.add(board[y][m]);
                    board[y][m] = 0;
                    break;
                }
            }
        }
        Collections.reverse(dolls);
        
        for (int dol: dolls){
            if (stack.isEmpty()){
                stack.push(dol);
            }
            else{
                if (stack.peek() == dol){
                    stack.pop();
                    ans += 2;
                }
                else{
                    stack.push(dol);
                }
            }
        }
        return ans;
    }
}