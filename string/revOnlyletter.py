s="a bc@def"
sl=list(s)
left=0
right=len(s)-1
while left<right:
    if ("a"<=sl[left]<="z")or("A"<=sl[left]<="Z")  :
        if ("a"<=sl[right]<="z")or("A"<=sl[right]<="Z"):
            sl[left],sl[right]=sl[right],sl[left]
            left+=1
            right-=1
        else:
            right-=1
    else:
        left+=1
s2="".join(sl)
print(s2)