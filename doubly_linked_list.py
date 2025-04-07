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
    
  def insert(self, element: str, index: int) -> None:
    if index < 0 or index > self._size:
      raise IndexError("Index out of range")
        
    new_node = Node(element)
        
    if index == 0:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    elif index == self._size:
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    else:
        current = self.head
        for _ in range(index):
            current = current.next
        
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
    
    self._size += 1