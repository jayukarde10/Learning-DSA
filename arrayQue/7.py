#two sum problem using two pointer approach
arr = [1, 3, 5, 7, 9]
target = 12
left=0
right=len(arr)-1
while left<right:
    s=arr[left]+arr[right]
    if s==target:
        print(f"{arr[left]}+{arr[right]}={target}")
        break
    elif s<target:
        left+=1
    else:
        right-=1