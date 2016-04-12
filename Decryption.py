# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:13:50 2016

@author: Aditya
"""

import hashlib

#declaration of all variables and list
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
tokens = []
encryptedValueList = []
hashedKeyList = []
temp = []
patternList = []
hashedKeyDecrypted = ''

#read the intermediate file
fp = open("intermediatefile.txt","r")
for i in fp.read().split(";;;"):
	tokens.append(i)

fp.close()

#save all the tokens in variables
filename = tokens[0]
encryptedValue = tokens[1]
encryptionPattern = tokens[2]
charactersCount = int(tokens[3])
numbersCount = int(tokens[4])



#now split the encrypted values
for i in encryptedValue.split('001100'):
	encryptedValueList.append(i)
encryptedValueList.pop()

#conversion of dec to bin
for i in encryptedValueList:
	temp.append(int(i,2))

#convert pattern to list
for i in encryptionPattern:
	patternList.append(int(i))

#conversion to from encryption to normal hashed key
i=0
while (i<len(patternList)):
	if patternList[i] == 1:
		hashedKeyList.append(characters[temp[i]-1])
	elif patternList[i] == 0:
		hashedKeyList.append(numbers[temp[i]])
	i+=1

#join the hashed key
for i in hashedKeyList:
	hashedKeyDecrypted += i

#creating hex digest of the message
filePointer = open(filename,"r")
hashedKeyWhichWasEncrypted = hashlib.sha256(filePointer.read()).hexdigest()
filePointer.close()

print "Hashed Key value (original): ",hashedKeyWhichWasEncrypted
print ""
print "Hased Key value (Decrypted): ",hashedKeyDecrypted
print ""

if hashedKeyWhichWasEncrypted == hashedKeyDecrypted:
	print "Success File is not tampered"
else:
	print "The file has been tampered"

print ""
