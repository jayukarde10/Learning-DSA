# Rotated Sorted Array
# Given a sorted array that has been rotated some number of times, find the index of a given element or target in the array. If the target is not found, return -1.
a=[4,5,6,7,8,0,1,2]
target=8
left=0
right=len(a)-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        print(mid)
        break
    # Left half sorted
    if a[left] <= a[mid]:

        if a[left] <= target < a[mid]:
            right = mid-1
        else:
            left = mid+1

    # Right half sorted
    else:

        if a[mid] < target <= a[right]:
            left = mid+1
        else:
            right = mid-1
else:
    print("not found")