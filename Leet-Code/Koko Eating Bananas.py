# Koko Eating Bananas
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


# Example 1:

# Input: piles = [3, 6, 7, 11], h = 8
# Output: 4

# Example 2:

# Input: piles = [30, 11, 23, 4, 20], h = 5
# Output: 30

# Example 3:

# Input: piles = [30, 11, 23, 4, 20], h = 6
# Output: 23

class Solution(object):
    def minEatingSpeed(self, piles, H):
        def canEatAll(time):
            return sum((p+time-1)/time for p in piles) <= H
        l = 1
        h = max(piles)

        while l<h:
            m = (l+h)/2
            if canEatAll(m):
                h = m
            else:
                l = m+1
        return l
