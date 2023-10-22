"""
simple sorting algorithm called Bubble Sort.
"""

def bubble_sort(arr):
    n = len(arr)
    total_swaps = 0
    
    for i in range(n):
        swaps = 0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                total_swaps += 1
                
        if swaps == 0:
            # If no swaps were made in this pass, the array is already sorted.
            break
    
    return total_swaps

# Read input
a = [4,3,2,1]
# n = int(input())
# a = list(map(int, input().split()))

# Sort the array using bubble sort and get the total number of swaps
num_swaps = bubble_sort(a)

# Print the required information

print(f"Array is sorted in {num_swaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")