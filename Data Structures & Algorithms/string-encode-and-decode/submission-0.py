class Solution:

    def encode(self, strs: List[str]) -> str:
        # first byte is the length of the list
        output: str = chr(len(strs))

        # for each string, append its length as a byte and the string itself
        for string in strs:
            output += chr(len(string)) + string
        
        return output

        


    def decode(self, s: str) -> List[str]:
        # first byte is the length of the list
        list_len: int = ord(s[0])

        ptr: int = 1 
        output: List[str] = []

        while ptr < len(s):
            # get the string length
            str_len: int = ord(s[ptr])
            ptr += 1

            # get the string
            output.append(s[ptr : ptr+str_len])
            ptr += str_len
        
        assert len(output) == list_len

        return output


        
