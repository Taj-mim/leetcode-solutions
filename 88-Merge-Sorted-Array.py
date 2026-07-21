class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:]=nums2
        nums1.sort()
        
nums1=list(map(int,input().split(',')))
m=int(input())
nums2=list(map(int,input().split(',')))
n=len(nums2)
sol=Solution()
sol.merge(nums1,m,nums2,n)
print(nums1)


""" for i in range(0,len(nums1)):
            for j in range(0,len(nums1)):
                if(nums1[i]==nums1[j]):
                    temp=nums1[i+1]
                    nums1[i+1]=nums1[j]
                    nums1[j]=temp

            

            
                    """