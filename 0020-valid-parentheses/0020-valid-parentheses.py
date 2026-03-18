class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '}':
                if not stack or stack[-1] != '{': stack.append('}')
                else: stack.pop()
            elif c == ']':
                if not stack or stack[-1] != '[': stack.append(']')
                else: stack.pop()
            elif c == ')':
                if not stack or stack[-1] != '(': stack.append(')')
                else: stack.pop()
            else: stack.append(c)
        return True if not stack else False