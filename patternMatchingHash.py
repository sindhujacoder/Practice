#Given a string and a pattern, write a program to find all occurences of the pattern in the string
#For example, string = "THIS IS A TEST TEXT", pattern = "TEST"
#Output = Pattern found at index 10
#Example 2, string =  "AABAACAADAABAABA", pattern =  "AABA"
#Output: Pattern found at index 0, Pattern found at index 9, Pattern found at index 12

##The naive approach would be to slide over the entire string in windows of length equal to the length of the pattern
#And check every cbaracter if it matches the pattern

def get_pattern_indexes(string, pattern):
  size = len(string)
  result = []
  pattern_size = len(pattern)
  for i in range(0, size):
    substring = string[i:i+pattern_size]
    if substring == pattern:
      result.append(i)
  
  return result


      