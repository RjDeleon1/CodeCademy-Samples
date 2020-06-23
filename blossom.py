from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.size = size
    self.array = [LinkedList() for i in range(self.size)]

  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.size
  
  def assign(self, key, value):
    payload = Node([key, value])
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
    list_at_array.insert(payload)
  
  def retrive(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
      else:
        return None
    
    if payload != None:
      if payload[0] == key:
        return payload[1]
      else:
        return None
    else:
      return None


blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

print(blossom.retrive('daisy'))
