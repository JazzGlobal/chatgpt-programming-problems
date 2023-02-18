# Problem given by Chat GPT
# Given a list of integers, write a function to find the longest subarray 
# where the absolute difference between any two adjacent elements is no greater than 1.

# Input:  [1,1,1,1,1]
# Expected Output: [1,1,1,1,1]

# Input: [1, 3, 3, 3, 2, 4, 4, 2, 1, 1]
# Output: [3,3,3,2]

def longest_subarray(nums):
    '''
    Returns the longest sub array where the absolute difference between any two adjacent elements is no greater than 1.
    '''
    max_sub_arr = {}
    start = 0
    for i in range(0, len(nums) - 1):
        if abs(nums[i] - nums[i+1]) > 1:
            max_sub_arr[start] = nums[start:i+1]
            start = i + 1
    
    max_sub_arr[start] = nums[start:i+2]

    maxList = max(max_sub_arr.values(), key=len)
    return maxList

# Problem given by Chat GPT
# Write a function that returns the second smallest integer in the list.

# Input:  [1,1,1]
# Expected Output: 1

# Input: [1, 1, 2]
# Output: 2
def second_smallest_num(nums):
    '''
    Returns the second smallest number in the given array.
    '''
    nums.sort()
    first_smallest = nums[0]
    for i in range(1, len(nums)):
        if first_smallest < nums[i]:
            return nums[i]
    return first_smallest

# Problem given by Chat GPT
# You are given an array of integers representing a sequence. You need to find the length of the longest increasing subsequence (LIS) of the sequence. 
# An increasing subsequence is a subsequence in which the elements are in increasing order, but not necessarily adjacent.

# Input:  [1, 2, 3, 0, 4, 5, 6]
# Expected Output: [1, 2, 3, 4, 5, 6]

# Input: [1, 3, 2]
# Output: [1, 3]
def largest_increasing_subsequence(nums, index=0, temp=[]):
    '''
    Returns the LIS found in a given number array.
    '''
    if (len(nums) == index):
        return temp

    sub_array = [nums[index]]
    smaller_num = nums[index]
    for i in range(index, len(nums) - 1):
        if smaller_num < nums[i+1]:
            smaller_num = nums[i+1]
            sub_array.append(nums[i+1])
    if len(temp) < len(sub_array):
        temp = sub_array
    return largest_increasing_subsequence(nums, index+1, temp) 