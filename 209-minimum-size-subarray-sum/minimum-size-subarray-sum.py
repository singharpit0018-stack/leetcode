class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        ml =float('inf')
        cnt=0
        
        for i in range (len(nums)):
            cnt +=nums[i]
            while cnt >=target:
                ml=min(ml,i-l+1)
                cnt-=nums[l]
                l+=1
        return 0 if ml ==float('inf')else ml   
        