from Node import Node, insert

def find_sum(root):
    if root is None:
        return 0
    return root.val + find_sum(root.left) + find_sum(root.right)

# Приклад використання
root = Node(10)
root = insert(root, 5)
root = insert(root, 20)
root = insert(root, 15)
root = insert(root, 25)

print("Сума всіх значень у дереві:", find_sum(root))
