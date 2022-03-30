class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # handle the silly edge case since we can't return a list
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif n == 0:
            return
        
        
        i = m - 1
        j = n - 1
        write = len(nums1) - 1
        
        # merge values until the end of one list is reached
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1
         
        # finish out the remaining values from either list
        while i >= 0:
            nums1[write] = nums1[i]
            i -= 1
            write -= 1
        
        while j >= 0:
            nums1[write] = nums2[j]
            j -= 1
            write -= 1
        

        