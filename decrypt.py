"""

LESSON
-- prev = ord(word[i]) => prev = current

Their messages consist of lowercase latin letters only, and every word is encrypted separately as follows:

Convert every letter to its ASCII value. Add 1 to the first letter, and then for every letter from the second one to the last one, add the value of the previous letter. Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII. Convert the values back to letters.

For instance, to encrypt the word crime

Decrypted message:	c	r	i	m	e
Step 1:	99	114	105	109	101
Step 2:	100	214	319	428	529
Step 3:	100	110	111	116	113
Encrypted message:	d	n	o	t	q
The FBI needs an efficient method to decrypt messages. Write a function named decrypt(word) that receives a string that consists of small latin letters only, and returns the decrypted word.

Explain your solution and analyze its time and space complexities.

Examples:

input:  word = "dnotq"
output: "crime"

input:  word = "flgxswdliefy"
output: "encyclopedia"

"""


def decrypt(word):
  if not word:
    return ""
  prev = ord(word[0])
  result = chr(prev-1)
  i=1
  while i<len(word):
    current = ord(word[i])-prev
    while current < ord('a'):
      current += 26
    result = result + chr(current)
    prev = ord(word[i])
    i+=1
  return result

print decrypt("dnotq") #crime
print decrypt("flgxswdliefy") #


def decrypt2(word):
    if not word:
        return ''
    result=chr(ord(word[0])-1)
    prev = ord(word[0])
    for i in range(1, len(word)):
        result = result+decryptChar(ord(word[i]), prev)
        prev = ord(word[i])
    return result

def decryptChar(c, prev):
    c = c - prev
    while c<ord('a'):
        c = c+26
    return chr(c)

print decrypt2("dnotq")