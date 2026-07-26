arr = [0,1,2,8,4]
left = 0
right = len(arr) - 1

while left <right:
    mid =(left+right)//2
     # Going uphill
    if arr[mid]< arr[mid+1]:
        left=mid+1
    # Going downhill
    else:
        right=mid
print("Peak Element:", arr[left])
print("Peak Element Index:", left)
