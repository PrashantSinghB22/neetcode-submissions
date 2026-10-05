class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            array = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                array[index] += 1
            key = tuple(array)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
