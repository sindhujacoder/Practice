

def reverseString_brute(string):
  #O(n) - Time Complexity
  reverse_string = []
  #O(n) - Space Complexity
  for i in range(len(string) - 1, -1, -1):
    reverse_string.append(string[i])
  
  return ''.join(reverse_string)

def swap(string, a, b): 
  string = list(string)
  temp = string[a]
  string[a] = string[b]
  string[b] = temp
  return ''.join(string)

def reverseString_ideal(string):
  #O(n) - Time Complexity
  #O(1) - Space Complexity
  for i in range(0, len(string)//2):
    string = swap(string, i, len(string)-i-1)
  return string
    
  return string