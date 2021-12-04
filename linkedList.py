class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
class LinkedList:
  def __init__(self, value):
    self.head = value;
    self.tail = value;
    self.length = 1