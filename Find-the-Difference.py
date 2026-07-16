"""
The main issue with this solution is its givving O(nlog n)time complexity to minimize time 
complexity it's better to use any other alternative solution which will minimize time 
complexity"""

class Solution:
    def findTheDifference(self, s, t):
        l1=sorted(s)
        l2=sorted(t)
        for i in range(0,len(s)):
            if(l2[i]!=l1[i]):
                return l2[i]
        return l2[-1]
s=input()
t=input()

sol =Solution()
print(sol.findTheDifference(s,t))


