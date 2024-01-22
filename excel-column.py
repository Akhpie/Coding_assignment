def convert_to_title(A):
    result = ""
    
    while A > 0:
        remainder = (A - 1) % 26
        result = chr(ord('A') + remainder) + result
        A = (A - 1) // 26
    
    return result

# Example usage:
input_1 = 1
input_2 = 28

output_1 = convert_to_title(input_1)
output_2 = convert_to_title(input_2)

print("Output 1:", output_1)
print("Output 2:", output_2)
