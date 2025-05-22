import java.util.*;

class Solution {
    public int solution(String s) {
        int len = s.length();
        s += s;
        int ans = 0;

        A: for (int i = 0; i < len; i++) {
            Deque<Character> stack = new ArrayDeque<>();
            for (int j = i; j < i + len; j++) {
                char c = s.charAt(j);
                if (c == ')' || c == '}' || c == ']') {
                    if (stack.isEmpty()) continue A;
                    char top = stack.peek();
                    if ((top == '(' && c == ')') ||
                        (top == '{' && c == '}') ||
                        (top == '[' && c == ']')) {
                        stack.pop();
                    } else {
                        continue A;
                    }
                } else {
                    stack.push(c);
                }
            }
            if (stack.isEmpty()) {
                ans++;
            }
        }
        return ans;
    }
}
