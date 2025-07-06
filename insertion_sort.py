def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
nums = [5, 2, 9, 1, 5, 6]
insertion_sort_desc(nums)
print("Sorted array (descending):", nums)

# Example 2
nums2 = [10, 20, 15, 30, 5]
insertion_sort_desc(nums2)
print("Sorted array (descending):", nums2)