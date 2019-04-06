# merge_sort.py
# Name: Sadisha Galappatti
# Date: March 27, 2019
# Algorithms textbook (CLRS) algorithms practice
import math

def merge_sort(A):
    if len(A) > 1:
        mid = int(math.floor((len(A)) / 2))
        left = A[:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)
        # A = merge(A[:mid], A[mid:])
        i, j, k = 0, 0, 0
        # min_left_right = min(len(left), len(right))
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
        return A


def main():
    input_array = [5,12,2,4,6,1,3,7,8,10,14,12,13,11,9]
    res = merge_sort(input_array)
    print(res)



if __name__ == "__main__":
    main()
