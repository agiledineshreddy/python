# sorting
# axis=0: Sorts along the columns. This means each column is sorted independently.
# axis=1: Sorts along the rows. This means each row is sorted independently.
# axis=0
import numpy as np
# Create a 2D array
arr = np.array([[ [9, 8, 7],[6, 5, 4],[3, 2, 1]],[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]])

print("Original array:")
print(arr)
sorted_axis_0 = np.sort(arr, axis=0)
print("\nSorted along columns (axis=0):")
print(sorted_axis_0)

sorted_axis_1 = np.sort(arr, axis=1)
print("\nSorted along rows (axis=1):")
print(sorted_axis_1)




print("Original array:")
print(arr)

# Quick Sort  :Quick Sort is the default sorting algorithm in NumPy. It's generally efficient for most datasets.
sorted_quick_axis_0 = np.sort(arr, axis=0, kind='quicksort')
sorted_quick_without_axis = np.sort(arr,kind='quicksort')
sorted_quick_axis_1 = np.sort(arr, axis=1, kind='quicksort')
print("\nQuick Sort along columns (axis=0):")
print(sorted_quick_axis_0)
print("\nQuick Sort along rows (axis=1):")
print(sorted_quick_axis_1)
print("\nsorted_quick_without_axis")
print(sorted_quick_without_axis)

# Merge Sort:: Merge Sort is a stable sorting algorithm, meaning that it maintains the relative order of equal elements. It's useful when stability is required.
sorted_merge_axis_0 = np.sort(arr, axis=0, kind='mergesort')
sorted_merge_without_axis = np.sort(arr, kind='mergesort')
sorted_merge_axis_1 = np.sort(arr, axis=1, kind='mergesort')
print("\nMerge Sort along columns (axis=0):")
print(sorted_merge_axis_0)
print("\nMerge Sort along rows (axis=1):")
print(sorted_merge_axis_1)
print("\nsorted_merge_without_axis")
print(sorted_merge_without_axis)

# Heap Sort::Heap Sort is an in-place, non-recursive sorting algorithm. It is not stable but is useful for large datasets where memory usage is a concern.
sorted_heap_axis_0 = np.sort(arr, axis=0, kind='heapsort')
sorted_heap_without_axis = np.sort(arr, kind='heapsort')
sorted_heap_axis_1 = np.sort(arr, axis=1, kind='heapsort')
print("\nHeap Sort along columns (axis=0):")
print(sorted_heap_axis_0)
print("\nHeap Sort along rows (axis=1):")
print(sorted_heap_axis_1)
print("\nsorted_heap_without_axis")
print(sorted_heap_without_axis)

