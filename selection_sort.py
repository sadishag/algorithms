# selection_sort.py
# Name: Sadisha Galappatti
# Date: March 27, 2019
# Algorithms textbook (CLRS) algorithms practice


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
