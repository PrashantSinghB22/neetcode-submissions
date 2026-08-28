class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += f"{len(word)}#{word}"
        return encoded_string
            

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = s.find("#", i)

            length = int(s[i:j])
            start = j + 1
            word = s[start: start + length]

            decoded.append(word)

            i = start + length

        return decoded
        



