def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter the number of terms: "))

if num <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Series:")
    for i in range(num):
        print(fibonacci(i), end=" ")