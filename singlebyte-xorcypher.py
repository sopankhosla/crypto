import base64
from string import *

def XORStrings(stringA, stringB):
	outputString = "" # Ouptut string is empty for now
	binaryA = stringA.decode("hex") # The plaintext of stringA
	binaryB = stringB.decode("hex") # The plaintext of stringB
	for x, y in zip(binaryA, binaryB): # Zip it up so each char has an XOR operator matched to it
		outputString += chr(ord(x) ^ ord(y)) # Append the result of the XOR as a character to the outputString
	return outputString

def isprintable(s):
	return all(a in printable for a in s)	

fp = open("challenge4.txt")
lines = fp.readlines()
for i in lines:
	for x in range(0, 150):
		val = str(XORStrings(i.strip(), str(x)*50))
		if isprintable(val):
			print chr(x), val # You need the '*34' bit so that you have equal length strings to XOR
# The single char key is ':', and it produces the message "Cooking MCs like a pound of bacon"
# Hopefully the next one will be "Burning em, you aint quick your nimble"
# I have been known to go crazy when I hear a cymbal and a highhat, with a suped up tempo
# I am on a roll, its time to go solo