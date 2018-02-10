'''
Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
'''
def deletion_distance(str1, str2):
  idx1 = 0
  idx2 = 0
  distance=0
  while idx1<len(str1) and idx2<len(str2):
      if str1[idx1]==str2[idx2]:
        idx1+=1
        idx2+=1
      elif idx1<len(str1)-1 and str1[idx1+1]==str2[idx2]:
        idx1 +=1
        distance +=1
      elif idx2<len(str2)-1 and str1[idx1]==str2[idx2+1]:
        idx2 +=1
        distance +=1
      else:
        idx1+=1
        idx2+=1
        distance +=2

  return distance + len(str2) - idx2 + len(str1) - idx1