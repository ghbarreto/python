def fun(n):
    if n > 1:
        return n  
    else:
        return(fun(n-1) + fun(n-2))

for i in range(10):
    print(fun(i))