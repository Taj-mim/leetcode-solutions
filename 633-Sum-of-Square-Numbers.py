"""Given a non-negative integer c, decide whether there're two integers a and b
such that a2 + b2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false

Constraints:
0 <= c <= 231 - 1 
"""
import math
class Solution(object):
    #this takse O(n) time complexity and O(1) space complexity brute force solution
    def judgeSquareSum(self, c, d):
        x=int(math.sqrt(c))
        for i in range(0,x+1):
            for j in range(0,x+1):
                if(i*i+j*j==c):
                    return True
        return False 


#now try to solve this problem using two pointer approach which will take O(sqrt(n)) time complexity
#  and O(1) space complexity
        left,right=0,int(math.sqrt(c))
        while(left<=right):
            if(left*left+right*right==c):
                return True
            elif(left*left+right*right<c):
                left+=1
            else:
                 right-=1
        return False
        """
        :type c: int
        :rtype: bool
        """


c=int(input())
d=int(input())
solution = Solution()
print(solution.judgeSquareSum(c,d))

#if i try to run this it will give me an error because i can only return one value from a function 
# but here i am trying to return two values from the function so i will have to comment out
#  the first or second solution and then run the code