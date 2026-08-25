class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        array = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            array[index] += 1
        for char in t:
            index = ord(char) - ord('a')
            array[index] -= 1
        
        for value in array:
            if value != 0:
                return False

        return True
        