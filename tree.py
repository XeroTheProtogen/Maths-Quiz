
class Node:
  """This 'Node' class implements the N-nary tree system,
    which will be used as an cleaner alternative to a Dictionary
    branch system."""
  """The N-nary tree is a data structure which stores data in a 'tree' of node
    which is divided into layers, with the first layer containing a 'root' node."""
    
  def __init__(self, n: int, data):
    #The information stored in the node
    self.data = data
    #Dynamic Array storing child nodes
    self.children=[None]*n

  def getLength(self) -> int:
    #How many children does this node have
    return len(self.children)

  def getCapacity(self) -> int:
    return self.n

def addQuestion(parent: Node, question, answer) -> Node:
  if parent.getCapacity() == 0:
    raise ValueError("Node must have capacity")
  
  l = parent.getLength()
  
  parent.children[l] = Node(2, f"Question {l + 1}")

  parent.children[l].children[0] = Node(0, question)
  parent.children[l].children[1] = Node(0, answer)

  return parent
