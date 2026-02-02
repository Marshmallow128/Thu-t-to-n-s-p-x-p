import numpy as np

def numpy_sort(arr):
    # Chuyển về numpy array và dùng hàm sort tích hợp
    return np.sort(np.array(arr))

if __name__ == "__main__":
    data = [82, 85, 88, 86, 90]
    print("Numpy Sort:", numpy_sort(data))