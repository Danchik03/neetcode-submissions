class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> List[str]:
        i=0
        lst = []
        while i < len(s):
            j=i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j+1
            end = start + length
            lst.append(s[start:end])
            i = end
        return lst
