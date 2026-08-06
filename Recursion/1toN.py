def l(n):
    if n==0 or n==1:
        return 1
    return n*l(n-1)

b=l(5)
print(b)

def fib(n):
    # Base Case
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive Case
    return fib(n - 1) + fib(n - 2)
0,1,1,2,3,5,8

n = 8
for i in range(n):
    print(fib(i),end=" ")


a, b = 0, 1

for _ in range(7):
    print(a, end=" ")
    a, b = b, a + b

print("--------------------")
def fun(n):
    print("Start", n)

    if n == 0:
        return

    fun(n-1)

    print("End", n)

fun(2) 