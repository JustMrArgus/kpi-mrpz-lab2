class ArrayList:
  def __init__(self):
    self.data = []
    self.size = 0
  
  def length(self) -> int:
    return self.size
  
  def append(self, element: str) -> None:
    if self.size == len(self.data):
      new_array = [None] * (max(1, self.size * 2))
      for i in range(self.size):
        new_array[i] = self.data[i]
      self.data = new_array
    
    self.data[self.size] = element
    self.size += 1
  
  def insert(self, element: str, index: int) -> None:
    if index < 0 or index > self.size:
      raise IndexError("Index out of range")
    
    if self.size == len(self.data):
      new_array = [None] * (max(1, self.size * 2))
      for i in range(self.size):
        new_array[i] = self.data[i]
      self.data = new_array
  
    for i in range(self.size, index, -1):
      self.data[i] = self.data[i-1]
    
    self.data[index] = element
    self.size += 1
  
  def delete(self, index: int) -> str:
    if index < 0 or index >= self.size:
      raise IndexError("Index out of range")
    
    removed_element = self.data[index]
    
    for i in range(index, self.size - 1):
      self.data[i] = self.data[i + 1]
    
    self.data[self.size - 1] = None
    self.size -= 1
    
    return removed_element
  
  def deleteAll(self, element: str) -> None:
    write_index = 0
    
    for i in range(self.size):
      if self.data[i] != element:
        self.data[write_index] = self.data[i]
        write_index += 1
    
    for i in range(write_index, self.size):
      self.data[i] = None
    
    self.size = write_index
  
  def get(self, index: int) -> str:
    if index < 0 or index >= self.size:
      raise IndexError("Index out of range")
    
    return self.data[index]
  
  def clone(self):
    new_list = ArrayList()
    
    new_list.data = [None] * max(1, self.size)
    
    for i in range(self.size):
      new_list.data[i] = self.data[i]
    
    new_list.size = self.size
    return new_list
  
  def reverse(self) -> None:
    for i in range(self.size // 2):
      temp = self.data[i]
      self.data[i] = self.data[self.size - 1 - i]
      self.data[self.size - 1 - i] = temp
  
  def findFirst(self, element: str) -> int:
    for i in range(self.size):
      if self.data[i] == element:
        return i
    return -1
  
  def findLast(self, element: str) -> int:
    for i in range(self.size - 1, -1, -1):
      if self.data[i] == element:
        return i
    return -1
  
  def clear(self) -> None:
    for i in range(self.size):
      self.data[i] = None
    self.size = 0
  
  def extend(self, elements) -> None:
    for i in range(elements.size):
      self.append(elements.data[i])
  
  def __str__(self):
    return str(self.data[:self.size])