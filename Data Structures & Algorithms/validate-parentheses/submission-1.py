class Solution:
    def isValid(self, s: str) -> bool:

        closeOpen = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for i in s:

            if i in closeOpen and stack:

                if (stack[-1] == closeOpen[i]):

                    stack.pop()
                
                else:

                    return False
            
            else:
                stack.append(i)

        if not stack:

            return True

        return False
        