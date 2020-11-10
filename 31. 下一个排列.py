'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        Len = len(nums)
        upper = 1
        for i in range(Len - 1):
            if nums[i+1] <= nums[i]:continue
            else: upper = 0
        if upper: return nums.reverse()
        # Max = [nums[-1], Len]
        for i in range(Len - 2, -1, -1):
            if nums[i] < nums[i+1]: 
                tarLeft = i
                break
        for i in range(Len - 1, -1, -1):
            if nums[i] > nums[tarLeft]:
                nums[i], nums[tarLeft] = nums[tarLeft], nums[i]
                break
        tarLeft += 1
        # 插入排序
        for insert_index, insert_value in enumerate(nums[tarLeft + 1:]):
            temp_index = insert_index
            while insert_index >= 0 and insert_value < nums[tarLeft + insert_index]:
                nums[tarLeft + insert_index + 1] = nums[tarLeft + insert_index]
                insert_index -= 1
            if insert_index != temp_index:
                nums[tarLeft + insert_index + 1] = insert_value


