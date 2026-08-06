def subsequence(arr, index, temp):
    if index == len(arr):  
        print(temp)
        return

    # Take
    temp.append(arr[index])
    subsequence(arr, index + 1, temp)
   # Backtrack
    temp.pop()
    # Don't Take
    subsequence(arr, index + 1, temp)

arr = [1, 2, 3]
subsequence(arr, 0, [])