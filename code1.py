class Node():
  def __init__(self, value, next):
    self.value=value
    self.next=next



class Linkedlist():
  def __init__(self):
    self.head=Node(0, None)
    one=Node(1, None)
    two=Node(2,None)
    three=Node(3,None)

    self.head.next=one
    one.next=two
    two.next=three
    

  def print_list(self):
    current=self.head
    while(current.next!=None):
      print(current.next.value)
      current=current.next

  def append_end(self,val):
    current=self.head
    while(current.next!=None):
      current=current.next
    new_node = Node(val,None)
    current.next = new_node
    

  def append_begin(self):
    five=Node(5,None)
    five.next = self.head.next
    self.head.next = five

  def search_node(self, value):
    current=self.head
    while(current.next!=None):
      if value == current.value:return True
      current = current.next
    if value == current.value:return True
    return False
     
    

  


sl=Linkedlist()
sl.append_end(4)
sl.append_begin()
sl.print_list()
print(sl.search_node(4))
