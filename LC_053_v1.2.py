# LC_053.py Maxumum-subarray problem
import numpy as np

"""
1017 / 1017 test cases passed.
Status: Accepted
Runtime: 84 ms
20.74
"""
class Solution(object):
    def Find_Max_Crossing_Subarray(self, A, low, mid, high):
        left_sum = -99999
        sum = A[mid]
        # print "sum=", sum
        for index in range(mid, low-1, -1):
            # print index, mid, low
            sum = sum + A[index]
            # print "sum=", sum
            if (sum > left_sum):
                left_sum = sum
                max_left = index
        # if (A[mid] >= left_sum):
        #     left_sum = A[mid]
        right_sum = -99999
        
        sum = A[mid]
        for index_r in range(mid+1, high+1, 1):
            # print index_r, mid+1, high
            sum = sum + A[index_r]
            if (sum > right_sum):
                right_sum = sum
                max_right = index_r
        # if (A[mid] >= righ_sum):
        #     righ_sum = A[mid]
        if (A[mid] >= right_sum and A[mid] >= left_sum):
            return A[mid]
        else:
            return left_sum+right_sum

        # return (max_left, max_right, left_sum+right_sum )


    def maxSubArray(self, A):
        """
        :type x: int
        :rtype: int
        """
        if (len(A) == 1 ):
            return A[0]
        elif (len(A) == 2):
            if A[0] > A[1]:
                return A[0]
            else:
                return A[1]
        else:
            # print "I am here"
            mid = (len(A)-1) / 2 
            # print "mid=", mid
            left_Solution = Solution()
            right_Solution = Solution()
            cross_Solution = Solution()
            # print A[:mid], (A[mid+1:])
            
            left_sum = left_Solution.maxSubArray(A[:mid])
            # print "left_sum= ", left_sum
            right_sum = right_Solution.maxSubArray(A[mid+1:])
            # print "right_sum= ", right_sum
            cross_sum = cross_Solution.Find_Max_Crossing_Subarray(A, 0,  mid, (len(A)-1))
            
            
            

            if (left_sum >= right_sum) and (left_sum >= cross_sum):
                return left_sum
            elif (right_sum >= left_sum) and (right_sum >= cross_sum):
                return right_sum
            else:
                return cross_sum



my_Solution = Solution()
print my_Solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# print my_Solution.Find_Max_Crossing_Subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4], 0, 4, 8)