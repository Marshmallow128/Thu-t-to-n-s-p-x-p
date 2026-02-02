def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Chạy thử
if __name__ == "__main__":
    data = [95, 120, 100, 98, 102]
    print("QuickSort:", quick_sort(data))