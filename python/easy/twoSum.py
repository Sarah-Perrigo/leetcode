"""
This program takes an array of integers nums and an integer target,
and returns indices of the two numbers that add up to target.
Can be assumed that each input only has one solution
Rating: Easy
Performance: Runtime O(N) -> Beats 82%, Memory beats 75%
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        length = len(nums)
        solution = []

        for i in range (length):
            if (target - nums[i]) in nums[i+1:length]:
                firstNumsLength = len(nums[0:i])
                secondNums = nums[i+1:length]
                solution.append(i)
                solution.append(secondNums.index(target - nums[i]) + firstNumsLength + 1)
                return solution
        return []

            

"""
    Performance: Runtime beats 58%, Memory beats 98%
    
    length = len(nums)
    solution = []

    for i in range (length):
        if (target - nums[i]) in nums[i+1:length]:
            firstNumsLength = len(nums[0:i])
            secondNums = nums[i+1:length]
            solution.append(i)
            solution.append(secondNums.index(target - nums[i]) + firstNumsLength + 1)
            return solution
    return []


        
    Brute Force:

    Performance: 

    for i in range (length):
    for j in range (first + 1, length):
        if (nums[i] + nums[j] == target):
            solution.append(i)
            solution.append(j)
            return solution
    """