import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

arr_plus_10 = arr + 10
print("After adding 10:", arr_plus_10)


arr_times_2 = arr * 2
print("After multiplying by 2:", arr_times_2)

# Calculate sum and mean
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
