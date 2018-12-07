class Node:
    @property
    def face_value(self):
        return sum([num for num in self.meta]) + sum([child.face_value for child in self.children])

    @property
    def full_value(self):
        if self.num_children == 0:
            return sum([num for num in self.meta])
        value = 0
        for num in self.meta:
            try:
                value += self.children[num - 1].full_value
            except IndexError:
                continue
        return value

    def __init__(self, num_children, num_meta):
        self.children = []
        self.meta = []
        self.num_children = num_children
        self.num_meta = num_meta

def build_tree(license_list):
    nodes = []
    index = iter(license_list)
    root = Node(next(index), next(index))
    nodes.append(root)
    while len(nodes) > 0:
        current_node = nodes.pop()
        if len(current_node.children) == current_node.num_children:
            for _ in range(current_node.num_meta):
                current_node.meta.append(next(index))
        else:
            new_node = Node(next(index), next(index))
            current_node.children.append(new_node)
            nodes.append(current_node)
            nodes.append(new_node)
    return root

file = open('./license.txt')
license_list = [int(num) for num in file.read().split(' ')]
root = build_tree(license_list)
print('Part A: {}'.format(root.face_value))
print('Part B: {}'.format(root.full_value))
