from Node import Node, insert

def find_max(root):
    current = root
    while current.right:
        current = current.right
    return current.val

root = Node(10)
root = insert(root, 5)
root = insert(root, 20)
root = insert(root, 15)
root = insert(root, 25)

print("Найбільше значення в дереві:", find_max(root))
