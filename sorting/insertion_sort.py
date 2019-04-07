# insertion_sort.py
# Name: Sadisha Galappatti
# Date: March 24, 2019
# Algorithms textbook (CLRS) algorithms practice

# read input function to read stdin and parse
def read_input(n):
    input = []
    for i in range(n):
        input.append(raw_input())
    return input

def insertion_sort(A):
    a_len = len(A)
    for i in range(1, a_len):
        key = A[i]
        j = i - 1
        while(j >= 0 and A[j] > key):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    print(A)

def reverse_insertion_sort(A):
    a_len = len(A)
    for i in range(1, a_len):
        key = A[i]
        j = i - 1
        while(j >= 0 and A[j] < key):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    print(A)

def main():
    # input_array = read_input(1)
    # input_array = input_array.split(" ")

    input_array = [5,12,2,4,6,1,3,7,8,10,14,12,13,11,9]
    insertion_sort(input_array)

    reverse_insertion_sort(input_array)




if __name__ == "__main__":
    main()
