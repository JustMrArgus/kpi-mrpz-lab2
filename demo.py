from array_list import ArrayList
from doubly_linked_list import DoublyLinkedList

def demonstrate_list(list_obj):
  
  print(f"Initial length: {list_obj.length()}")
  list_obj.append('A')
  list_obj.append('B')
  list_obj.append('C')
  print(f"After appending A, B, C - Length: {list_obj.length()}")
  print(f"List contents: {list_obj}")
  
  list_obj.insert('D', 1)
  print(f"After inserting D at position 1: {list_obj}")
  
  print(f"Element at position 0: {list_obj.get(0)}")
  print(f"Element at position 1: {list_obj.get(1)}")
  
  deleted = list_obj.delete(2)
  print(f"Deleted element at position 2 ({deleted}): {list_obj}")
  
  list_obj.append('A')
  print(f"After appending another A: {list_obj}")
  print(f"First A is at position: {list_obj.findFirst('A')}")
  print(f"Last A is at position: {list_obj.findLast('A')}")
  
  list_obj.deleteAll('A')
  print(f"After deleting all A's: {list_obj}")
  
  clone = list_obj.clone()
  print(f"Original list: {list_obj}")
  print(f"Cloned list: {clone}")
  
  other_list = type(list_obj)()
  other_list.append('X')
  other_list.append('Y')
  list_obj.extend(other_list)
  print(f"After extending with [X, Y]: {list_obj}")
  
  list_obj.reverse()
  print(f"After reversing: {list_obj}")
  
  list_obj.clear()
  print(f"After clearing - Length: {list_obj.length()}")
  print(f"List contents: {list_obj}")

def main():
  print("DEMONSTRATING ARRAY-BASED LIST")
  array_list = ArrayList()
  demonstrate_list(array_list)
  
  print("\n" + "="*50 + "\n")
  
  print("DEMONSTRATING DOUBLY LINKED LIST")
  linked_list = DoublyLinkedList()
  demonstrate_list(linked_list)

if __name__ == "__main__":
  main()
