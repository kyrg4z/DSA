class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        right = 0
        
        for left in range(1, len(nums)):
            if nums[left] != nums[right]:
                right += 1
                nums[right] = nums[left]
        
        return right + 1