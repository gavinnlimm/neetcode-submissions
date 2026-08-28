class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        openingBracket = "([{"
        closingBracket = ")]}"

        for i in range(len(s)): 
            if s[i] in openingBracket: 
                stack.append(s[i])
            elif s[i] in closingBracket:
                if not stack:
                    return False
                if s[i] == ")" and stack.pop() != "(":
                    return False
                if s[i] == "]" and stack.pop() != "[":
                    return False
                if s[i] == "}" and stack.pop() != "{":
                    return False
            
        return not stack ## ensures that it is empty stack and all open and closing matches
                    



