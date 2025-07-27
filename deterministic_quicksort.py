# deterministic_quicksort.py

def quicksort(arr):
    def _quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            _quicksort(arr, low, pivot_index - 1)
            _quicksort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    arr_copy = arr.copy()
    _quicksort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

# Test
if __name__ == "__main__":
    test_array = [8, 4, 23, 42, 16, 15]
    print("Original:", test_array)
    print("Sorted:", quicksort(test_array))
