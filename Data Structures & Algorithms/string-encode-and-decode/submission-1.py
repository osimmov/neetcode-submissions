class Solution:
    def encode(self, strs: List[str]) -> str:
        union = ""
        point = [0]

        for i in strs:
            union += i
            point.append(len(union))
        
        return ",".join(map(str, point)) + "|" + union

    def decode(self, s: str) -> List[str]:
        # your code
        point_str, strs = s.split("|")
        point = list(map(int, point_str.split(",")))

        arr = []
        for i in range(1, len(point)):
            arr.append(strs[point[i-1]:point[i]])
        
        return arr
