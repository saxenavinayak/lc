class Solution:
    def removeStars(self, s: str) -> str:
        mystack = []

        for char in s:
            if char != "*":
                mystack.append(char)
            else:
                mystack.pop()
    
        return "".join(mystack)


"""
[l,e,e,t]
[l,e,e,""]

"""
        

