#!/usr/bin/env python3

### imports for program
import string
import sys
from operator import itemgetter

##################################################################################
### function implementations
##################################################################################

# scoreString: Iterates through byte strings, and assigns a score based on english
#              character frequency chart
# parameters: byteString is the string to be scored
# return: score for byteString -- establishes how likely it is to contain english 
#         words
def scoreString(byteString):

	charFrequencies = {
		'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
	}

	return sum([charFrequencies.get(chr(byte), 0) for byte in byteString.lower()])

# decrypt: bitwise XOR of input string against possible single-char key values
# parameters: hexVal is the string to be brute-force decrypted
# return: list of possibly decrypted byte strings
def decrypt(hexVal):

	possible = string.printable

	scores = []
	for possibleKey in possible:
		decrypted = b''

		for byte in hexVal:
			decrypted += bytes([int(byte)^ord(possibleKey)])
			
		score = scoreString(decrypted)
		scores.append([decrypted, score])

	scored = sorted(scores, key=itemgetter(1), reverse=True)
	return scored

# printDecryptedStrings: prints possible decrypted strings, sorted highest score
#                        to lowest
# parameters: scoredStrings
# return: prints strings to console
def printDecryptedStrings(scoredStrings):

	for decrypted in scoredStrings:
		print(decrypted[0].decode("ascii"))

##################################################################################
### Main entry point for program
##################################################################################

# main: main-entry point for brute-force single-char-XOR decryption
#       usage: ./xorBruteForce.py <hex value>
# parameters: n/a
# return: prints possible decrypted strings
def main():

	userInput = str(sys.argv[1])
	hexString = bytes.fromhex(userInput)

	possibleStrings = decrypt(hexString)
	printDecryptedStrings(possibleStrings)

if __name__ == '__main__':

	main()
