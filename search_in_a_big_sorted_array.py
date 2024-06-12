"""
[LintCode 447] Search in a Big Sorted Array
Link: https://www.lintcode.com/problem/search-in-a-big-sorted-array

Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).
Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.
Return -1, if the number doesn't exist in the array.
"""

class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        i = 0
        while reader.get(i) < target:
            i = i * 2 + 1

        l = i // 2
        r = i

        while l <= r:
            mid = l + (r-l) // 2
            if reader.get(mid) == target:
                r = mid - 1
            elif reader.get(mid) > target:
                r = mid - 1
            elif reader.get(mid) < target:
                l = mid + 1

        return l if reader.get(l) == target else -1
