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

  def delete(self, index: int) -> str:
    if self.head is None or index < 0 or index >= self._size:
      raise IndexError("Index out of range")
    
    if index == 0:
      data = self.head.data
      if self.head == self.tail:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.next
        self.head.prev = None
      self._size -= 1
      return data
    
    if index == self._size - 1:
      data = self.tail.data
      self.tail = self.tail.prev
      self.tail.next = None
      self._size -= 1
      return data
    
    current = self.head
    for _ in range(index):
      current = current.next
    
    data = current.data
    current.prev.next = current.next
    current.next.prev = current.prev
    self._size -= 1
    return data
  
  def deleteAll(self, element: str) -> None:
    if self.head is None:
      return
    
    current = self.head
    while current:
      next_node = current.next
      if current.data == element:
        if current == self.head:
          self.head = current.next
          if self.head:
              self.head.prev = None
          else:
              self.tail = None
        elif current == self.tail:
          self.tail = current.prev
          self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        self._size -= 1
      current = next_node
    
  def get(self, index: int) -> str:
    if index < 0 or index >= self._size:
      raise IndexError("Index out of range")
  
    current = self.head
    for _ in range(index):
      current = current.next
  
    return current.data
  
  def clone(self):
    new_list = DoublyLinkedList()
    current = self.head
    while current:
      new_list.append(current.data)
      current = current.next
    return new_list
  
  def reverse(self) -> None:
    if self.head is None or self.head == self.tail:
      return
    
    current = self.head
    self.tail = self.head
    
    while current:
      temp = current.next
      current.next = current.prev
      current.prev = temp
      
      if not current.prev:
        self.head = current
      current = current.prev
  
  def findFirst(self, element: str) -> int:
    current = self.head
    index = 0
    
    while current:
      if current.data == element:
        return index
      current = current.next
      index += 1
    
    return -1

  def findLast(self, element: str) -> int:
    current = self.tail
    index = self._size - 1
    
    while current:
      if current.data == element:
        return index
      current = current.prev
      index -= 1
    
    return -1
  
  def clear(self) -> None:
    self.head = None
    self.tail = None
    self._size = 0
  
  def extend(self, elements) -> None:
    if isinstance(elements, DoublyLinkedList):
      current = elements.head
      while current:
        self.append(current.data)
        current = current.next
    else:
      for i in range(elements.length()):
        self.append(elements.get(i))
  
  def __str__(self):
    if self.head is None:
      return "[]"
      
    result = "["
    current = self.head
      
    result += "'" + str(current.data) + "'"
    current = current.next
      
    while current:
      result += ", '" + str(current.data) + "'"
      current = current.next
      
    result += "]"
    return result