"""
202 / 202 test cases passed.
Status: Accepted
Runtime: 66 ms
35.47%
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -9999999
        temp_sum = 0
        # print ""

        for index in range(0, len(nums), 1):
        	# print index, nums[index]
        	if (temp_sum > 0):
        		temp_sum += nums[index]
        	else:
        		temp_sum = nums[index]
        	if temp_sum > max_sum:
        		max_sum = temp_sum
        	print "index, temp_sum ,max_sum = ", index, temp_sum, max_sum
        return max_sum


my_Solution = Solution()

# print my_Solution.maxSubArray([2, -7, 4, -3, 6, 4, -4, 1, -5, 0])
print my_Solution.maxSubArray([2, -7, 4, -3, 6, 4, -4, 1, -5, 0])        
