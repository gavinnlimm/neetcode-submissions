class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += str(len(s)) + "#" + s
        
        return encodedString
    
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # 1. find the '#' starting from position i
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
        
            snew = s[j+1 : j+1+length]
            result.append(snew)
            
            i = j + 1 + length
        
        return result


                    

