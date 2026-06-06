class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        
        while begin <= end:
            
            mid = (begin + end) // 2  
            
            if target == nums[mid]:
                
                return mid  
            elif target < nums[mid]:
                end = mid - 1
            else:
                begin = mid + 1
    
        return begin
