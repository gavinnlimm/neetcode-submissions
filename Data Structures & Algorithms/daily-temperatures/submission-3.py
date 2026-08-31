class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []     # holds indices of unresolved days

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop() 
                result[prev] = i - prev # days before

            stack.append(i) # appends index of unresolved days

        return result

