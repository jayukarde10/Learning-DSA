arr = [10, 20, 30, 40, 50]
target = 40
for i in arr:
    if i == target :
        print(f"found at position {arr.index(i)}")
    else :
        print("not found")