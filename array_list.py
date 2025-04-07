class ArrayList:
  def __init__(self):
    self.data = []
  
  def length(self) -> int:
    return len(self.data)
  
  def append(self, element: str) -> None:
    self.data.append(element)