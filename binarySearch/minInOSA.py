a=[4,5,6,7,8,0,1,2]
target=float('inf')
left=0
right=len(a)-1
while left<=right:
    mid=(left+right)//2
    # Left half sorted
    if a[left] <= a[mid]:
        target=min(target,a[left])
        left = mid+1
    # Right half sorted
    else:
        target=min(target,a[mid])
        right = mid-1
print(target)
