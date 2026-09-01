class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stack of the temperatures
        #if we hit a temperature thats warmer than the top of the stack, we can pop until the next element to pop is greater
        #we also keep track of a count here

        stack = []
        answer = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            count = 0
            
            while stack and stack[-1][1] < t: #this means the newest day is WARMER
                #we pop until this isn't true, increment the count, update the array there
                index = stack[-1][0]
                answer[index] = (i - index)
                
                #we cant rely on a count, we need to know the index that they had
                stack.pop()
            
            stack.append((i, t))

        return answer