class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        # Initialize two arrays to store products to the left and right of each element
        left_products = [1] * n
        right_products = [1] * n
        
        # Calculate products to the left of each element
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            left_products[i] = left_product
        
        # Calculate products to the right of each element
        right_product = 1
        for i in range(n - 2, -1, -1):
            right_product *= nums[i + 1]
            right_products[i] = right_product
        
        # Multiply left and right products for the final result
        answer = [left_products[i] * right_products[i] for i in range(n)]
        
        return answer