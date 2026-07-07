class Solution:
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    def letterCombinations(self, digits: str) -> List[str]:

        if (len(digits) == 1):
            return self.mapping[digits]
        else:
            ret = []
            current_chars = self.mapping[digits[0]]
            for char in current_chars:
                down_one = self.letterCombinations(digits[1:])
                for s in down_one:
                    ret.append(char+s)
            return ret

