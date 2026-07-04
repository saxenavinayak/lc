# String Compression
class Solution:
    def compress(self, chars: List[str]) -> int:

        current_compression_candidate_char = chars[0]
        compression_start_index = 0
        output_compression_string = 0
        chars.append("!")
        for i in range(len(chars)):
            if (chars[i] == current_compression_candidate_char):
                continue
            elif (chars[i] != current_compression_candidate_char):
                # We have reached a point to compress a string
                length_of_compressed_string = i - compression_start_index
                if length_of_compressed_string == 1:
                    string_to_add = current_compression_candidate_char
                else:
                    string_to_add = current_compression_candidate_char + str(length_of_compressed_string)
                for char in string_to_add:
                    chars[output_compression_string] =  char
                    output_compression_string += 1

                current_compression_candidate_char = chars[i]
                compression_start_index = i
        return output_compression_string


