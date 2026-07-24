""" 
Given two integer arrays and , return nums1 nums2 an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4] 
Output: [9,4]
Explanation: [4,9] is also accepted.
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        x1=set(nums1)
        x2=set(nums2)
        return list(x1.intersection(x2))


num1=list(map(int,input().split(',')))
num2=list(map(int,input().split(',')))
sol=Solution()
print(sol.intersection(num1,num2))