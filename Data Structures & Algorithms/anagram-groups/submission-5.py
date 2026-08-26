class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = {}
        
        for word in strs:
            array = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                array[index] += 1

            key = tuple(array)    
            
            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]

        for value in seen.values():
            result.append(value)
        
        return result
        
        


        


        




        
        