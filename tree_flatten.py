class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution(object):
    def flatten(self, root: TreeNode) -> None:
        tmp = root.right
        root.right = root.left
        root.left = tmp

        if root.right.left is None:
            root.right.right = root.left
        if root.right.right is not None:
            self.flatten(root.right)




    def createTree(self):
        root = TreeNode(1)
        root.right = TreeNode(5)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)

        self.flatten(root)

        print(str(root.val))
        print(str(root.right.val))
        print(str(root.right.right.val))
        print(str(root.right.right.right.val))
        print(str(root.left.val))


if __name__ == "__main__":
    sol = Solution()
    sol.createTree()
