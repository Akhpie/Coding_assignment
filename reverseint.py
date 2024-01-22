def reverse_integer(x):
    sign = 1 if x >= 0 else -1
    x = abs(x)
    
    reversed_num = 0
    while x != 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    
    reversed_num *= sign
    
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if reversed_num > INT_MAX or reversed_num < INT_MIN:
        return 0
    
    return reversed_num

input_1 = 123
input_2 = -123

output_1 = reverse_integer(input_1)
output_2 = reverse_integer(input_2)

print("Output 1:", output_1)
print("Output 2:", output_2)
