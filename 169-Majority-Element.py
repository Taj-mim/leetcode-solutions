"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
Example 1:

Input: nums = [3,3,4]
Output: 3
"""
from collections import Counter

num=list(map(int,input().split(',')))
freq=Counter(num)
maxcount=max(freq.values())
most_common_values=freq.most_common(1)[0][0]
#most_common_values = [key for key, val in freq.items() if val == maxcount]  this is for multiple value if occur same timess

print(most_common_values)