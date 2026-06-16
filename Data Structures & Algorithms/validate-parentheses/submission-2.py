class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedtoOpen = {"}": "{", ")": "(", "]":"["}

        for char in s:
            if char in closedtoOpen:
                if stack and stack[-1] == closedtoOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False
            
            
