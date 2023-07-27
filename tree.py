
class Node:
  def __init__(self, n, data):
    self.data = data
    self.children=[None]*n

def inorder(node: Node):
  if node == None:
    return

  total = len(node.children)

  for i in range(total-1):
    inorder(node.children[i])

  print(node.data, end=" ")

  inorder(node.children[total-1])

def test():
  n = 3
  root = Node(n, 1)
  root.children[0] = Node(n, 2)
  root.children[1] = Node(n, 3)
  root.children[2] = Node(n, 4)
  root.children[0].children[0] = Node(n, 5)
  root.children[0].children[1] = Node(n, 6)
  root.children[0].children[2] = Node(n, 7)

  inorder(root)

