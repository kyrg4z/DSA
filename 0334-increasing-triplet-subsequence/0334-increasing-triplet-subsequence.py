class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                # x > first and x > second
                return True

        return False