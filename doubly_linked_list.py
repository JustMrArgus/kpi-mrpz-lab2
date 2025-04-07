class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0
  
  def length(self) -> int:
    return self._size
  
  def append(self, element: str) -> None:
    new_node = Node(element)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
      self._size += 1