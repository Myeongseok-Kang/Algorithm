import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        for (char c: s.toCharArray()){
            if (c == '('){stack.push('(');}
            else {
                if (stack.isEmpty()){return false;}
                else {stack.pop();}
            }
        }
        if (stack.isEmpty()){return true;}
        else{return false;}
    }
}