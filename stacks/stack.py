# stack.py
# Name: Sadisha Galappatti
# Date: April 7, 2019

class Stack:

    # Give an array can be empty
    def __init__(self, arr):
        self.stack_arr = arr

    # Lets assume we don't have append
    # Create a tmp array of size len(stack_arr) + 1
    # Add value n to the newly created index
    def push(self, n):
        stack_arr_len = len(self.stack_arr)
        tmp = [None] * (stack_arr_len + 1)
        tmp[:stack_arr_len] = self.stack_arr[:stack_arr_len]
        tmp[-1] = n
        self.stack_arr = tmp
        return self.stack_arr


    # Implementing pop, needs to remove the element from the array
    # Python arrays have a pop method but this is how I would
    # write it.
    def pop(self):
        last_element = self.stack_arr[-1]
        self.stack_arr = self.stack_arr[:len(self.stack_arr)-1]
        return last_element



if __name__ == "__main__":
    st = Stack([])
    print(str(st.push(3)))
    print(str(st.push(9)))
    print(str(st.push(14)))
    print(str(st.pop()))
    print(str(st.stack_arr))
