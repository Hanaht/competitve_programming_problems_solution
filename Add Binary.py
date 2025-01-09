class Solution:
    def addBinary(self, a: str, b: str) -> str:
        z=bin(int(a,2)+int(b,2))
        z=(z[2:])
        return z
