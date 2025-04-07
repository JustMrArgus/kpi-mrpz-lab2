import unittest
from array_list import ArrayList
from doubly_linked_list import DoublyLinkedList

class TestArrayList(unittest.TestCase):
  def setUp(self):
    self.list = ArrayList()

  def test_length(self):
    self.assertEqual(self.list.length(), 0)
    self.list.append("a")
    self.assertEqual(self.list.length(), 1)

    # Just comment to show that CI/CD works fine

  def test_append(self):
    self.list.append("x")
    self.assertEqual(str(self.list), "['x']")

  def test_insert(self):
    self.list.append("a")
    self.list.insert("b", 0)
    self.assertEqual(str(self.list), "['b', 'a']")

  def test_delete(self):
    self.list.append("a")
    removed = self.list.delete(0)
    self.assertEqual(removed, "a")
    self.assertEqual(self.list.length(), 0)

  def test_deleteAll(self):
    for el in ["a", "b", "a", "c"]:
      self.list.append(el)
    self.list.deleteAll("a")
    self.assertEqual(str(self.list), "['b', 'c']")

  def test_get(self):
    self.list.append("test")
    self.assertEqual(self.list.get(0), "test")

  def test_clone(self):
    self.list.append("a")
    cloned = self.list.clone()
    self.assertEqual(str(cloned), "['a']")
    self.assertIsNot(cloned, self.list)

  def test_reverse(self):
    for el in ["a", "b", "c"]:
      self.list.append(el)
    self.list.reverse()
    self.assertEqual(str(self.list), "['c', 'b', 'a']")

  def test_findFirst(self):
    for el in ["x", "y", "x"]:
      self.list.append(el)
    self.assertEqual(self.list.findFirst("x"), 0)

  def test_findLast(self):
    for el in ["x", "y", "x"]:
      self.list.append(el)
    self.assertEqual(self.list.findLast("x"), 2)

  def test_clear(self):
    self.list.append("x")
    self.list.clear()
    self.assertEqual(self.list.length(), 0)

  def test_extend(self):
    other = ArrayList()
    other.append("a")
    other.append("b")
    self.list.extend(other)
    self.assertEqual(str(self.list), "['a', 'b']")

class TestDoublyLinkedList(unittest.TestCase):
  def setUp(self):
    self.list = DoublyLinkedList()

  def test_length(self):
    self.assertEqual(self.list.length(), 0)
    self.list.append("a")
    self.assertEqual(self.list.length(), 1)

  def test_append(self):
    self.list.append("x")
    self.assertEqual(str(self.list), "['x']")

  def test_insert(self):
    self.list.append("a")
    self.list.insert("b", 0)
    self.assertEqual(str(self.list), "['b', 'a']")

  def test_delete(self):
    self.list.append("x")
    removed = self.list.delete(0)
    self.assertEqual(removed, "x")
    self.assertEqual(self.list.length(), 0)

  def test_deleteAll(self):
    for el in ["a", "b", "a", "c"]:
      self.list.append(el)
    self.list.deleteAll("a")
    self.assertEqual(str(self.list), "['b', 'c']")

  def test_get(self):
    self.list.append("test")
    self.assertEqual(self.list.get(0), "test")

  def test_clone(self):
    self.list.append("a")
    cloned = self.list.clone()
    self.assertEqual(str(cloned), "['a']")
    self.assertIsNot(cloned, self.list)

  def test_reverse(self):
    for el in ["a", "b", "c"]:
      self.list.append(el)
    self.list.reverse()
    self.assertEqual(str(self.list), "['c', 'b', 'a']")

  def test_findFirst(self):
    for el in ["x", "y", "x"]:
      self.list.append(el)
    self.assertEqual(self.list.findFirst("x"), 0)

  def test_findLast(self):
    for el in ["x", "y", "x"]:
      self.list.append(el)
    self.assertEqual(self.list.findLast("x"), 2)

  def test_clear(self):
    self.list.append("x")
    self.list.clear()
    self.assertEqual(self.list.length(), 0)

  def test_extend(self):
    other = DoublyLinkedList()
    other.append("a")
    other.append("b")
    self.list.extend(other)
    self.assertEqual(str(self.list), "['a', 'b']")

if __name__ == '__main__':
    unittest.main()
