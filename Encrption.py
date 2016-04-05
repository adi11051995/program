# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:55:38 2016

@author: Aditya
"""

#importing hashing library
import hashlib

#take the filename as input
filename = raw_input("Enter the filename: ")

#creating hex digest of the message
filePointer = open(filename,"r")
hashedKey = hashlib.sha256(filePointer.read()).hexdigest()
filePointer.close()

print hashedKey
#declaration of all variables and list
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
charactersNumbersBinary = []
encryptedValueList = []
encryptedValueBinaryList = []
charactersCount = 0
numbersCount = 0
charactersNumbersValue = ''

#encryption
#create binary values for occurences of chars and numbers
for i in hashedKey:
	if characters.__contains__(i):
		charactersCount+=1
		charactersNumbersBinary.append(1)
		encryptedValueList.append(characters.index(i)+1)
	elif numbers.__contains__(i):
		numbersCount+=1
		charactersNumbersBinary.append(0)
		encryptedValueList.append(int(i))

print charactersNumbersBinary
print encryptedValueList
for i in charactersNumbersBinary:
	charactersNumbersValue += str(i)
print charactersNumbersValue
#function to convert decimal to binary values
def dec_to_bin(x):
    	temp = int(bin(x)[2:])
    	return temp

#encrypt values by converting them to binary values
for i in encryptedValueList:
	encryptedValueBinaryList.append(dec_to_bin(i))	
print encryptedValueBinaryList
encryptedKey = ''

for i in encryptedValueBinaryList:
	encryptedKey += str(i) + '001100'
print encryptedKey

#save the content in an intermediatery file
fp = open("intermediatefile.txt","w")
fp.write(filename+';;;'+encryptedKey+';;;'+charactersNumbersValue+';;;'+str(charactersCount)+';;;'+str(numbersCount))
fp.close()

print hashedKey
