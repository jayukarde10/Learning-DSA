arr = [1,2,3,3,4]
target = 3
left=0
right=len(arr)-1
ans=-1
while left<=right:
    mid=(right+left)//2
    if arr[mid]==target:
        ans=mid
        left=mid+1
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print(ans)