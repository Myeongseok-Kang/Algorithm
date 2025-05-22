import java.util.*;

class Solution
{
    public int solution(String s)
    {
        /*
        문자열 길이 1 -> return 0
        
        스택에 맨앞 문자 넣고
        맨앞 제외 문자열 순회 (c)
            스택빔 -> 그냥 넣음
            else
                스택 peek 와 c 같으면 -> pop
                다르면 -> 스택에 넣기
        스택빔 -> 1
        아님 -> 0
        */
        if (s.length() == 1) return 0;
        Deque<Character> stack = new ArrayDeque<>();
        stack.push(s.charAt(0));
        for (char c: s.substring(1).toCharArray()){
            if (stack.isEmpty()){stack.push(c);}
            else {
                if (stack.peek() == c){stack.pop();}
                else {stack.push(c);}
            }
        }
        return stack.isEmpty()? 1: 0;
    }
}