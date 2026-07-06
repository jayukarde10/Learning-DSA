l=["flower","flow","flight"]
smallest = min(l, key=len)
ans=""
for i in range(len(smallest)):
    for j in l:
        if j[i] != smallest[i]:
            print(ans)
            exit() #Stop the entire program immediately 
    ans+=smallest[i]
print(ans)
    



