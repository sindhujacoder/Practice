#map_ = {1:2, 2:3, 3:4}
#collisions occur with enough data n limited space
#O(n/k) , k=len(hashmap) 
#resolve collision - separate chaining, open address, round robin 

#Now although there are some for loops running in the class hash,
#the time complexity is not O(n).
#This is because n stands for the size of the input, which corresponds to number of key,value pairs in the table
#But the for loop in the _hash function runs only for the length of the key, which would be insignificantly small in comparison to the number of entries in general.
#Also, the for loop in the get function runs for the length of the collisioned array, which in most cases, won't be too long
#Atleast nowhere near to the number of total entries, hence the time complexity remains way less than O(n), even less than O(log n) in most cases
#The keys and values methods are slightly worse than O(n) though, as we have to loop over the entire size of the table once,
#And loop over all the lists in the buckets which have collision

class hashTable():
  def __init__(self, size):
    self.size = size
    self.data = [None] * size
  
  def _hash(self, key):
    hash = 0
    for i in range(1, len(key)):
      hash = (hash + ord(key[i]) * i)  % self.size
    return hash
  
  def set(self, key, value):
    hash = self._hash(key)
    if self.data[hash] == None:
      self.data[hash] = [[key, value]]
    else:
      self.data[hash].append([key, value])
  
  def get(self, key):
    hash = self._hash(key)
    if self.data[hash]:
      for i in range(0, len(self.data[hash])):
        if self.data[hash][i][0] == key:
          return self.data[hash][i][1]
    return None
  
  def keys(self):
    keys_ = []
    for i in range(len(self.data)):
      if self.data[i] != None:
        for j in range(0, len(self.data[i])):
          keys_.append(self.data[i][j][0])
    return keys_

  def values(self):
    values_ = []
    for i in range(len(self.data)):
      if self.data[i] != None:
        for j in range(0, len(self.data[i])):
          values_.append(self.data[i][j][0])
    return values_



      
