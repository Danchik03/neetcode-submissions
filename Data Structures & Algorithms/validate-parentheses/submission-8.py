class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
        ")": "(",
        "]": "[",
        "}": "{"}
        arr=[]
        for i in s:
            if i in close_to_open:
                if len(arr) == 0:
                    return False
                nearest_opened = arr.pop()
                if nearest_opened != close_to_open[i]:
                    return False
            else:
                arr.append(i)
        return len(arr) == 0

            
        