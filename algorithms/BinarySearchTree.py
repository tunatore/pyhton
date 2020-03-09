class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert_node(self, node_root, val):
        if self.root is None:
            self.root = Node(val)
        else:
            if val <= node_root.val:
                if node_root.left is None:
                    node_root.left = Node(val)
                else:
                    self.insert_node(node_root.left, val)
            elif val > node_root.val:
                if node_root.right is None:
                    node_root.right = Node(val)
                else:
                    self.insert_node(node_root.right, val)

    def insert(self, val):
        self.insert_node(self.root, val)

    def find(self, val):
        return self.find_node(self.root, val)

    def find_node(self, node_root, val):
        if val == node_root.val:
            return True
        elif val < node_root.val:
            if node_root.left is None:
                return False
            else:
                return self.find_node(node_root.left, val)
        else:
            if node_root.right is None:
                return False
            else:
                return self.find_node(node_root.right, val)

    def print_in_order(self, node_root):
        if node_root.left is not None:
            self.print_in_order(node_root.left)
        print(node_root.val, end="->")
        if node_root.right is not None:
            self.print_in_order(node_root.right)

    def print_pre_order(self, node_root):
        print(node_root.val, end="->")
        if node_root.left is not None:
            self.print_pre_order(node_root.left)
        if node_root.right is not None:
            self.print_pre_order(node_root.right)

    def print_post_order(self, node_root):
        if node_root.left is not None:
            self.print_post_order(node_root.left)
        if node_root.right is not None:
            self.print_post_order(node_root.right)
        print(node_root.val, end="->")

    def print_breadth_first_search(self, root):
        if root is None:
            return

        q = deque()
        q.append(root)

        while not len(q) == 0:
            node = q.popleft()
            print(node.val, end="->")
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    def print_breadth_first_recursive(self, nodes_queue):
        if nodes_queue is None or len(nodes_queue) == 0:
            return

        n = nodes_queue.popleft()
        print(n.val, end="->")

        if n.left is not None:
            nodes_queue.append(n.left)
        if n.right is not None:
            nodes_queue.append(n.right)
        self.print_breadth_first_recursive(nodes_queue)

    def print_depth_first(self, root):
        if root is None:
            return

        node_stack = []
        node_stack.append(root)

        while len(node_stack) != 0:
            node = node_stack.pop()
            print(node.val, end="->")
            if node.right is not None:
                node_stack.append(node.right)
            if node.left is not None:
                node_stack.append(node.left)

    def print_depth_first_recursive(self, root):
        if root is None:
            return

        print(root.val, end="->")
        if root.left is not None:
            self.print_depth_first_recursive(root.left)
        if root.right is not None:
            self.print_depth_first_recursive(root.right)


b = BinarySearchTree()
b.insert(10)
b.insert(3)
b.insert(2)
b.insert(6)
b.insert(18)
b.insert(16)
b.insert(25)

print("find 6:", b.find(6))
print("find 10:", b.find(10))
print("find 8:", b.find(8))

print("in order:")
b.print_in_order(b.root)
print("\npre order:")
b.print_pre_order(b.root)
print("\npost order:")
b.print_post_order(b.root)
print("\nbreadth first search:")
b.print_breadth_first_search(b.root)
print("\nbreadth first search - recursive:")
q = deque()
q.append(b.root)
b.print_breadth_first_recursive(q)
print("\ndepth first search:")
b.print_depth_first(b.root)
print("\ndepth first search - recursive:")
b.print_depth_first_recursive(b.root)
