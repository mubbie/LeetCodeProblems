class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        special_char = "#"

        for item in strs:
            length = len(item)
            output += str(length) + special_char + item

        return output


    def decode(self, s: str) -> List[str]:
        output = []
        idx = 0
        special_char = "#"

        while idx < len(s):
            sp_char_idx = s.find(special_char, idx)
            length = int(s[idx:sp_char_idx])
            og_string = s[sp_char_idx+1 : sp_char_idx+length+1]
            output.append(og_string)
            print(output, sp_char_idx, length, og_string)
            idx = sp_char_idx+length+1

        return output