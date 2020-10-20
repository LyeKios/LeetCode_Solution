class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
#         list = []
#         count0 = 0
#         for i in nums:
#             if not i:
#                 list.insert(0, i)
#                 count0 += 1
#             if i == 1: list.insert(count0, i)
#             if i == 2: list.append(2)
#         nums = list


# class Solution:
#     def sortColors(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         # all in [0, zero] = 0
#         # all in (zero, i) = 1
#         # all in (two, len - 1] = 2

#         def swap(nums, index1, index2):
#             nums[index1], nums[index2] = nums[index2], nums[index1]

#         size = len(nums)
#         if size < 2:
#             return

#         zero = -1
#         two = size - 1

#         i = 0

#         while i <= two:
#             if nums[i] == 0:
#                 zero += 1
#                 swap(nums, i, zero)
#                 i += 1
#             elif nums[i] == 1:
#                 i += 1
#             else:
#                 swap(nums, i, two)
#                 two -= 1
