from avl_tree import insert


# Завдання №1
def find_min(root):
    if root is None:
        return None

    while root.left:
        root = root.left

    return root


# Завдання №2
def find_max(root):
    if root is None:
        return None

    while root.right:
        root = root.right

    return root


# Завдання №3
def find_sum(root):
    if root is None:
        return 0

    return root.key + find_sum(root.left) + find_sum(root.right)


def main():
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)

    print(f"Мінімальний ключ у дереві: {find_min(root).key}")
    print(f"Максимальний ключ у дереві: {find_max(root).key}")
    print(f"Сума всіх ключів у дереві: {find_sum(root)}")


if __name__ == "__main__":
    main()
