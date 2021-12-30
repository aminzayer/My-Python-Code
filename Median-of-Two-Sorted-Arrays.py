class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if (n > m):
            return self.findMedianSortedArrays(nums2, nums1)

        start = 0
        end = n
        realmidinmergedarray = (n + m + 1) // 2

        while (start <= end):
            mid = (start + end) // 2
            leftAsize = mid
            leftBsize = realmidinmergedarray - mid

            leftA = nums1[leftAsize - 1] if (leftAsize > 0) else float('-inf')
            leftB = nums2[leftAsize - 1] if (leftBsize > 0) else float('-inf')
            rightA = nums1[leftAsize] if (leftAsize < n) else float('inf')
            rightB = nums2[leftAsize] if (leftBsize < m) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if ((m + n) % 2 == 0):
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                return max(leftA, leftB)

            elif (leftA > rightB):
                end = mid - 1
            else:
                start = mid + 1


# Driver code
ans = Solution()
arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]
print("Median of the two arrays is {}".format(ans.Median(arr1, arr2)))

