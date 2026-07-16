"""
As using sorted method and iterate the function using loop give O(nlog n)
To mitimize that it's better to use ASCII value order 
"""
class Solution:
    def findTheDifference(self,s,t):
        sum1=0
        sum2=0
        for i in s :
            sum1=sum1+ord(i)
        for i in t :
            sum2=sum2+ord(i)
        return chr(sum2-sum1)

s = input()
t=input()
sol=Solution()
print(sol.findTheDifference(s,t))
