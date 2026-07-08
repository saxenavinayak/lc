class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pancake = []
        output = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            while ((len(pancake) > 0) and (temperatures[i] > temperatures[pancake[-1]])):
                output[pancake[-1]] = i - pancake[-1]
                pancake.pop()
            pancake.append(i)

        return output


        
