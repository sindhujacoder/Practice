

def mergeSortedArray(arr1, arr2):
  new_array = []
  flag = 0
  first_array_index = second_array_index = 0
  while(first_array_index < len(arr1) and second_array_index < len(arr2) ):
    if arr1[first_array_index] < arr2[second_array_index]:
      new_array.append(arr1[first_array_index])
      first_array_index += 1
    else:
      new_array.append(arr2[second_array_index])
      second_array_index += 1

    if first_array_index == len(arr1):
      flag = 1
  
  if flag == 1:
    new_array.extend(arr2[second_array_index:])
  else:
    new_array.extend(arr1[first_array_index:])

  return new_array