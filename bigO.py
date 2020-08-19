import time
def findNemo(arr):
  start_time = time.time()
  for each in arr:
    if each == 'nemo':
      print('found nemo')
  end_time = time.time()
  print((end_time - start_time))

def print_(arr):
  start_time = time.time()
  print(arr[0])
  end_time = time.time()
  print((end_time - start_time))

#What is the Big O of the below function? (Hint, you may want to go line by line)
def funChallenge(arr):
  a = 10; #O(1)
  a = 50 + 3; #O(1)
  for i in range(0, len(arr)): # O(n)
    print_(arr) # O(n)
    stranger = True # O(n)
    a+=1 # O(n)

  return a, stranger # O(1)
#O(3 + 4n) = O(n)  

