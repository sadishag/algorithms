# linked_list.py
# Name: Sadisha Galappatti
# Date: April 7, 2019

class Node:

    # Give an array can be empty
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self, root):
        res_str = ""
        while root != None:
            res_str += str(root.val)
            if root.next != None:
                res_str += "-->"
            root = root.next
        print(res_str)



if __name__ == "__main__":
    nd = Node(1)
    nd.next = Node(2)
    nd.next.next = Node(3)
    nd.next.next.next = Node(4)
    nd.next.next.next.next = Node(19)
    nd.print_list(nd)
