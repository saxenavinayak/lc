class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word_1_map = {}
        word_2_map = {}

        for char in word1:
            word_1_map[char] = word_1_map.get(char, 0) + 1
        for char in word2:
            word_2_map[char] = word_2_map.get(char, 0) + 1

        return (word_1_map.keys() == word_2_map.keys()) and (sorted(word_1_map.values()) == sorted(word_2_map.values()))

        # Return if numbers and letters are same within hashmap
        """
        word1 = "cabbba", word2 = "abbccc"
        word1 = "1c 2a 3b" word2 = "1a 2b 3c"

        """
