# 217. Contains Duplicate

# class Solution(object):
#     def containsDuplicate(self, nums):
#         newHash = []
#         for num in nums:
#             if num in newHash:
#                 return False
#             newHash[num] = "Whatever"
#         return True

# 238. Product of Array Except Self

# class Solution(object):
#     def productExceptSelf(self, nums):
#         newArr = []
#         for i, num in enumerate(nums):
#             deleted = nums.pop(i)
#             product = 1
#             for item in nums:
#                 product *= item
#             newArr.append(product)
#             nums.insert(i, deleted)
#         return newArr

# SOLUCION DE "238." MUY LENTA DEBE "mejorarse", queda pendiente

# 53. Maximum Subarray

# class Solution:
#     def maxSubArray(self, nums):
#         maxSub = nums[0]
#         curSum = 0
#         for n in nums:
#             if curSum < 0:
#                 curSum = 0
#             curSum += n
#             maxSub = max(maxSub, curSum)
#         return maxSub

# solucion = Solution()

# solucion(-3 , 5, 6 , -6, 5, -4)


# 152. Maximum Product Subarray

class Solution(object):
    def maxProduct(self, nums):
        result = max(nums)
        curMax, curMin = 1, 1
        
        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1
                continue
            tmp    = curMax*n
            curMax = max(n*curMin, n*curMax, n)
            curMin = min(n*curMin, tmp, n)
            result = max(result, curMax)
        return result

arr = [ -2, 3,-5, -2, 6,-3]
solucion = Solution()

print(solucion.maxProduct(arr))