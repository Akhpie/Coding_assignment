def is_prime(n):
    if n <= 1:
        return 0 
    elif n == 2:
        return 1 
    elif n % 2 == 0:
        return 0  

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return 0  

    return 1 

number = int(input("Enter a number: "))
result = is_prime(number)

if result:
    print(f"{number} is prime.")
else:
    print(f"{number} is not prime.")
