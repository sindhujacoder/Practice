#from bigO import findNemo, funChallenge
#O(n) --> Linear [FAIR]
#findNemo(['nemo']) #O(1)
#arr = ['nemo'] * 1000 #O(1000)
#findNemo(arr)
#arr = ['nemo'] * 100000 #O(10000)
#findNemo(arr) 
#print_(arr) # O(1) == O(2) == O(3) 
#funChallenge(arr)

#from bigO import print_ 
#from list import print_
#O(1) ---> constant time[Excellent]
#print_()

#from implement_array import myArray
#my_new_array = myArray()
#print(my_new_array.data)
#my_new_array.push('a')
#my_new_array.push('b')
#my_new_array.push('c')
#my_new_array.push('d')
#my_new_array.push('f')
#my_new_array.push('g')
#print(my_new_array.data)
#my_new_array.insert(4, 'e')
#print(my_new_array.data)
#print(my_new_array.pop())
#print(my_new_array.get(5))
#print(my_new_array.delete(5))
#print(my_new_array.data)
'''
from reverseString import reverseString_brute, reverseString_ideal

string = 'hdbgjelbeb'
reverse = reverseString_brute(string)
print(reverse)
reverse = reverseString_ideal(string)
print(reverse)

from check import smarter_reverse

string = 'hdbgjelbeb'
print(smarter_reverse(string))

from mergeSortedArrays import mergeSortedArray

arr1 = [1,3,5,7,9,11,13,15,17]
arr2 = [2,4,6,8,10,12,14,16]

print(mergeSortedArray(arr1, arr2))

arr1 = [8, 9, 10]
arr2 = [1]

print(mergeSortedArray(arr1, arr2))
'''
from implement_hashTable import hashTable

hash_obj = hashTable(10)
hash_obj.set('one', 1)
hash_obj.set('two', 2)
hash_obj.set('three', 3)
hash_obj.set('four', 4)
hash_obj.set('five', 5)
hash_obj.set('six', 6)

print(hash_obj.get('five'))
print(hash_obj.values())
print(hash_obj.keys())

from firstRecurringCharacterHash import get_first_recurring_char

arr = [4,5,6,7,4,6,7]
print(get_first_recurring_char(arr))

from patternMatchingHash import get_pattern_indexes

string1 = 'AABAACAADAABAABA'
print(get_pattern_indexes(string1, 'AABA'))
