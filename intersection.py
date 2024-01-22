def find_intersection(arr1, arr2):
    intersection = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return intersection

# Example usage:
arr1 = list(map(int, input("Enter sorted array 1: ").split()))
arr2 = list(map(int, input("Enter sorted array 2: ").split()))

result = find_intersection(arr1, arr2)
print("Intersection:", result)
