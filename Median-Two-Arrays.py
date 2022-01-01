#  Python 3 Program
#  Find median of two sorted arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s1 = len(nums1)
        s2 = len(nums2)
        first = 0
        second = 0
        counter = 0
        result = 0
        temp = 0
        while (counter <= int((s1 + s2) / 2)):
            temp = result
            if (first < s1 and second < s2):
                if (nums1[first] < nums2[second]):
                    result = nums1[first]
                    first += 1
                else:
                    result = nums2[second]
                    second += 1
            elif(first < s1):
                result = nums1[first]
                first += 1
            else:
                result = nums2[second]
                second += 1
            counter += 1
        if ((s1 + s2) % 2 != 0):
            return result
        else:
            result = int((result + temp) / 2)
            return result

class MyArray:
	# Function which is display array elements
	def display(self, arr, size):
		i = 0
		while (i < size):
			print(" ", arr[i], end="")
			i += 1

		print("\n", end="")

	# Find the median of given two sorted arrays
	def median(self, arr1, arr2):
		# Get the size of array
		s1 = len(arr1)
		s2 = len(arr2)
		# This two variables indicate index of arr1 and arr2
		first = 0
		second = 0
		# This variable are used to control loop
		counter = 0
		# This variables are used to store result
		result = 0
		temp = 0
		# Calculating median of given two sorted arrays
		while (counter <= int((s1 + s2) / 2)):
			# Get current calculated result
			temp = result
			if (first < s1 and second < s2):
				# When both array elemement exist
				if (arr1[first] < arr2[second]):
					# When first array element are small
					result = arr1[first]
					first += 1
				else:
					# When second array element are small
					result = arr2[second]
					second += 1

			elif(first < s1):
				result = arr1[first]
				first += 1
			else:
				result = arr2[second]
				second += 1

			counter += 1

		print(" First Array : ", end="")
		self.display(arr1, s1)
		print(" Second Array : ", end="")
		self.display(arr2, s2)
		if ((s1 + s2) % 2 != 0):
			print(" Median : ", result, " \n\n", end="")
		else:
			print(" Median Elements [", result, " ", temp, "] \n", end="")
			result = int((result + temp) / 2)
			print(" Median : ", result, " \n\n", end="")


def main():
	obj = MyArray()
	# When provide similar size of array elements
	a1 = [1, 2, 10]
	a2 = [4, 15, 16]
	obj.median(a1, a2)
	# When given
	a3 = [3, 11, 14]
	a4 = [6, 7, 22, 24]
	obj.median(a3, a4)
	a6 = [-3, 5, 8, 9]
	a7 = [-6, -5, -3, -1, 9, 13]
	obj.median(a6, a7)


if __name__ == "__main__": main()