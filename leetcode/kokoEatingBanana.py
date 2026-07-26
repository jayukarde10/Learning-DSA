import math

def minEatingSpeed(piles, h):

    left = 1
    right = max(piles)

    while left < right:

        mid = (left + right) // 2

        total = 0

        for bananas in piles:
            total += math.ceil(bananas / mid)

        if total <= h:
            right = mid      # Try a smaller speed
        else:
            left = mid + 1   # Need a faster speed

    return left


piles = [3, 6, 7, 11]
h = 8

print("Minimum Speed:", minEatingSpeed(piles, h))