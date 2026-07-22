arr = [3, 7, 10, 15, 20, 24, 31, 42, 56]
target=32
left = 0
right = len(arr) - 1

while left <= right:
    mid =(left+right)//2 # instead of int((left+right)/2) can use abs()
    if arr[mid] == target:
        print("found at",mid)
        break
    elif arr[mid] < target:
        left=mid+1
    else:
        right=mid-1
else:
    print("not found")
        

        
        
    

