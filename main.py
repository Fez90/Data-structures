"""class Array():
    def __init__(self,length,data):
        self.length = 0
        self.data = {}

    def get(self,index):
        return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length += item
        return self.length

newArray = Array(0,0)
newArray.push('hi')"""

""" def foo():
    return foo()

foo()"""
# Stack example
class Stack:
  def __init__(self):
    self.arr = []
    self.length = 0
  
  def __str__(self):
    return str(self.__dict__)
  
  def peek(self):
    return self.arr[self.length-1]

  def push(self,value):
    self.arr.append(value)
    self.length += 1

  def pop(self):
    popped_item = self.arr[self.length-1]
    del self.arr[self.length-1]
    self.length -= 1
    return popped_item

mystack = Stack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
print(mystack)
x = mystack.peek()
print(x)
mystack.pop()
print(mystack)
mystack.pop()
print(mystack)


# Queue example
class Node:
  def __init__(self,val):
    self.val = val
    self.next = None

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0 

  def peek(self):
    return self.first.val
  
  def enqueue(self,val):
    new_node = Node(val)
    if self.first == None:
      self.first = new_node
      self.last = self.first
      self.length += 1
    else:
      self.last.next = new_node
      self.last = new_node
      self.length += 1
  
  def dequeue(self):
    temp = self.first.next
    dequeued_element = self.first
    if temp == None:
      self.first = None
      self.length -= 1
      return 
    self.first.next = None
    self.first = temp
    self.length -= 1

  def printt(self):
    temp = self.first
    while temp != None:
      print(temp.val , end = '->')
      temp = temp.next
    print()
    print(self.length)

myq = Queue()
myq.enqueue('google')
myq.enqueue('microsoft')
myq.enqueue('facebook')
myq.enqueue('apple')
myq.printt()
# myq.dequeue()
# myq.printt()
x = myq.peek()
# print(x)