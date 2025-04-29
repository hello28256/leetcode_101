# -*-coding: utf-8 -*-
# @Time    : 2025/4/29 9:56
# @Author  : hello28256@gmail.com
# @FileName: 88_merge_sorted_array.py
# @Software: PyCharm
# @Blog    ：https://github.com/hello28256
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        pos=m+n-1
        m-=1
        n-=1
        while m>=0 and n>=0:
            if nums1[m]>nums2[n]:
                nums1[pos]=nums1[m]
                m-=1
            else:
                nums1[pos]=nums2[n]
                n-=1
            pos-=1
        nums1[:n+1]=nums2[:n+1]


if __name__=="__main__":
    solution=Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution.merge(nums1, 3, nums2, 3)
    print(nums1)
