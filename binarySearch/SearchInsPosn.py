# arr = [1,3,5,7]    jay logic bot it is linear not binary
# target = 2
# small=0
# big=0
# while big<=len(arr)-1:
#     if arr[small]==target:
#         print("target is in arr at posn",small)
#     elif arr[small]<target and big<len(arr):
#         small+=1        
#     big+=1
# else:
#     arr.insert(small,target)
#     print(arr)
    
arr = [1,3,5,7,9]
target=6
left = 0
right = len(arr) - 1

while left <= right:
    mid =(left+right)//2 # instead of int((left+right)/2)
    if arr[mid] == target:
        print("found at",mid)
        break
    elif arr[mid] < target:
        left=mid+1
    else:
        right=mid-1
else:
    arr.insert(left,target)
    print(arr)
