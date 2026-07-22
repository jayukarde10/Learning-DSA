arr = [1,2,3,3,4,6]
target=3
left=0
right=len(arr)-1

while left<=right:
    mid = (left+right) // 2

    if arr[mid]<target:
        left=mid+1
    else:
        right=mid-1

print("Lower Bound Index:", left)