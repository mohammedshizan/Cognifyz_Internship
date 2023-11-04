def fibonacci(n):
    if n<=0:
        return "Invalid input"
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    else:
        fib_series = fibonacci(n-1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
    
    
n=int(input("Enter the number:"))
result = fibonacci(n)
print(result)

    
    