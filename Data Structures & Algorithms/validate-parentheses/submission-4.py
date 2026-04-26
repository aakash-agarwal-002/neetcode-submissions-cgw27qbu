class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return True
        if len(s)==1:
            return False
        stack = []
        for i in range(len(s)):
            print(stack)
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                stack.append(s[i])
            elif stack:
                if s[i] == "]" and stack[-1]=="[":
                    stack.pop()
                elif s[i] == ")" and stack[-1]=="(":
                    stack.pop()
                elif s[i] == "}" and stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            else:
                return False
        return True if not stack else False
            
            