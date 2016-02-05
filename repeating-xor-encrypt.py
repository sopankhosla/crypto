import base64
from string import *
import binascii

def XORStrings(stringA, stringB):
	outputString = "" # Ouptut string is empty for now
	for x, y in zip(stringA, stringB): # Zip it up so each char has an XOR operator matched to it
		outputString += chr(ord(x) ^ ord(y)) # Append the result of the XOR as a character to the outputString
	return outputString


fp = open("challenge5.txt")

hexA = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
hexB = "ICE"
result = ""

for x in range(0, len(hexA)):
	result= result+str(XORStrings(hexA[x], hexB[x%3]))

print result.encode("hex")
