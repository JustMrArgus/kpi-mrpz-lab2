class ArrayList:
  def __init__(self):
    self.data = []
  
  def length(self) -> int:
    return len(self.data)
  
  def append(self, element: str) -> None:
    self.data.append(element)
  
  def insert(self, element: str, index: int) -> None:
    if index < 0 or index > len(self.data):
      raise IndexError("Index out of range")
    self.data.insert(index, element)