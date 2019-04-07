# selection_sort.py
# Name: Sadisha Galappatti
# Date: March 27, 2019
# Algorithms textbook (CLRS) algorithms practice

# 2.2-2
# Consider sorting n numbers stored in array A by first finding the smallest element
# of A and exchanging it with the element in AŒ1. Then find the second smallest
# element of A, and exchange it with AŒ2. Continue in this manner for the first n1
# elements of A. Write pseudocode for this algorithm, which is known as selection
# sort. What loop invariant does this algorithm maintain? Why does it need to run
# for only the first n  1 elements, rather than for all n elements? Give the best-case
# and worst-case running times of selection sort in ‚-notation.



# loops through the array, searches for minimum number and switches
# with the first value
# Runtime = O(n**2)
def selection_sort(A):
    a_len = len(A)
    for j in range(a_len):
        min = A[j]
        min_index = j
        for i in range(j+1,a_len):
            if A[i] < min:
                min = A[i]
                min_index = i
        A = switch_locations(A, j, min, min_index)
    print(A)


def switch_locations(A, index, min, min_index):
    tmp = A[index]
    A[index] = min
    A[min_index] = tmp
    return A


def main():
    input_array = [5,12,2,4,6,1,3,7,8,10,14,12,13,11,9]
    selection_sort(input_array)



if __name__ == "__main__":
    main()
