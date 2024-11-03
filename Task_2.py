from Node import Node, insert

def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current.val

root = Node(10)
root = insert(root, 5)
root = insert(root, 20)
root = insert(root, 15)
root = insert(root, 25)

print("Найменше значення в дереві:", find_min(root))
