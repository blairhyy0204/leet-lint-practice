"""
Questions on finding n elements in an array whose sum is equal to target.

Return all the non-redundant possible combination. The array contains redundant elements.
"""
from typing import List

def twoSum(target, nums, start):
    # TC: O(NlogN)
    nums = sorted(nums)
    i, j = start, len(nums) - 1
    res = []
    while i <= j:
        if nums[i] + nums[j] == target:
            res.append([nums[i], nums[j]])
            new_i = i+1
            while new_i < len(nums) and nums[new_i] == nums[i]:
                new_i += 1
            i = new_i 
            new_j = j - 1
            while new_j > -1 and nums[new_j] == nums[j]:
                new_j -= 1
            j = new_j
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return res

def nSum(n: int, target: int, nums: List[int], start: int):
    res = []
    if len(nums) < n or n < 2:
        return res

    if n == 2:
        return twoSum(target, nums, start)
     
    x = start
    while x < len(nums):
        sub = nSum(n-1, target-nums[x], nums, x+1)

        for a in sub:
            a.append(nums[x])
            res.append(a)
        new_x = x
        while new_x < len(nums) and nums[new_x] == nums[x]:
            new_x += 1
        x = new_x

    return res


if __name__ == "__main__":
    x = nSum(2, 4, [1,1,1,1,2,2,3,3,3], 0)
    print(x)


    


