class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

# Пример дерева:     4
#                  /   \
#                 2     6
root = Node(4)
root.left = Node(2)
root.right = Node(6)
inorder(root)  # 2 4 6