def insertion_sort(listt):
    for j in range(1, len(listt)):
        key = listt[j]
        i = j - 1
        while i >= 0 and listt[i] > key:
            listt[i+1] = listt[i]
            i -= 1
        listt[i+1] = key


def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    l1 = [None] * n1
    l2 = [None] * n2

    for i in range(0, n1):
        l1[i] = arr[p + i]

    for j in range(0, n2):
        l2[j] = arr[q + 1 + j]

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            arr[k] = l1[i]
            i += 1
        else:
            arr[k] = l2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = l1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = l2[j]
        j += 1
        k += 1


def merge_sort(arr, p, r):
    if p < r:
        q = p + (r - p) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


def counting_sort(listt, k):
    # all the elements are smaller than k
    arr = [0] * k
    for i in listt:
        arr[i] += 1
    sorted_list = [None] * len(listt)
    for i in range(1, k):
        arr[i] += arr[i-1]
    for j in range(len(listt)):
        sorted_list[arr[listt[j]]-1] = listt[j]
        arr[listt[j]] -= 1
    return sorted_list


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def delete(self, val):
        if self is None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def search(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.search(val)

        if self.right is None:
            return False
        return self.right.search(val)


class Node:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree:
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = 0
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    # Search the tree
    def search_tree(self, node, key):
        if node == self.nil or key == node.item:
            return node

        if key < node.item:
            return self.search_tree(node.left, key)
        return self.search_tree(node.right, key)

    # Balancing the tree after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def delete(self, node, key):
        z = self.nil
        while node != self.nil:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.nil:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.nil
        node.right = self.nil
        node.color = 1

        y = None
        x = self.root

        while x != self.nil:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root

    def delete_node(self, item):
        self.delete(self.root, item)

    def __print_helper(self, node, indent, last):
        if node != self.nil:
            print(indent)
            if last:
                print("R----")
                indent += "     "
            else:
                print("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def print_tree(self):
        self.__print_helper(self.root, "", True)


bst = RedBlackTree()

bst.insert(55)
bst.insert(40)
bst.insert(65)
bst.insert(60)
bst.insert(75)
bst.insert(57)

bst.print_tree()

print("\nAfter deleting an element")
bst.delete_node(40)
bst.print_tree()


tree = RedBlackTree()
for x in range(1, 15):
    tree.insert(x)
tree.print_tree()


nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
bst = BSTNode()
for num in nums:
    bst.insert(num)

nums = [2, 6, 20]
print("deleting " + str(nums))
for num in nums:
    bst.delete(num)
print("#")

print("4 exists:")
print(bst.search(4))
print("2 exists:")
print(bst.search(2))
print("12 exists:")
print(bst.search(12))
print("18 exists:")
print(bst.search(18))


a = [5, 2, 4, 1, 6, 3]
insertion_sort(a)
print(a)

b = [2, 4, 8, 1, 3, 7]
merge_sort(b, 0, (len(b)-1))
print(b)

c = [2, 5, 3, 0, 2, 3, 0, 3]
c1 = counting_sort(c, 6)
print(c1)
