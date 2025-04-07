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
  
  def delete(self, index: int) -> str:
    if index < 0 or index >= len(self.data):
      raise IndexError("Index out of range")
    return self.data.pop(index)
  
  def deleteAll(self, element: str) -> None:
    self.data = [item for item in self.data if item != element]
  
  def get(self, index: int) -> str:
    if index < 0 or index >= len(self.data):
      raise IndexError("Index out of range")
    return self.data[index]