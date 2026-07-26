def reverse(arr, left, right):
    # base Case
    if left>=right:
        return 
    # swap
    arr[left],arr[right]=arr[right],arr[left]
    # recursive call
    reverse(arr,left+1, right-1)


arr = [1,2,3,4,5]
reverse(arr,0,len(arr)-1)
print(arr)