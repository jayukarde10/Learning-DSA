arr = [5,9,8,7,9]
num=float('-inf')
num2=float('-inf')
for i in arr:
    if num<i :
        num=i
    elif num>i>num2  :
        num2=i
print(num,num2)