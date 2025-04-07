import unittest
from array_list import ArrayList
from doubly_linked_list import DoublyLinkedList

class TestArrayList(unittest.TestCase):
  def setUp(self):
    self.list = ArrayList()

class TestDoublyLinkedList(unittest.TestCase):
  def setUp(self):
    self.list = DoublyLinkedList()