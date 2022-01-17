# XOR Brute Force

**Description:**

This python script tries to crack a single-key XOR encryption with brute forcing techniques.

## xorBruteForce.py 

Building upon our understanding of xor encryption, we will now introduce the concept of the key when it comes to this type of encryption. Essentially, this `key` will be used to both encrypt and decrypt data. It does so by xor-ing each bit by the key, thus making this key the crucial piece of information to figure out when trying to crack this implementation. 

To start off, we will assume that the ciphertext is English, and will be a legible message for the purpose of the assignment. Thanks to data studies of the English language, there is a chart that will help us map the frequencies of each letter (on average) given a legitimate piece of English text. We can leverage this chart to analyze the strings that our algorithm will process. We will be sorthing the strings from *most-likely* to be English to *least-likely*.

### English Character Frequencies
```python
charFrequencies = {
	'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
}
```
> For example, the letter `a` will show up as 8.167% of the text, given legitimate English words

Our goal is to craft a function that will take a byte string as a parameter, analyze the string based on the chart, and assign it a score that we will use to sort the output. Thanks to list comprehensions and the `sum()` function, we can do so in one line.
```python
return sum([charFrequencies.get(chr(byte), 0) for byte in byteString.lower()])
```

Now that we have established a method to analyze a piece of English text, we need to now implement the decryption and guess the single-character key used. A good starting point in gathering the data set that will be used as the `possible` key, would be any printable character. Luckily, the built-in `string` module in Python3 can handle this elegantly with `string.printable`. 

From there, all we need to do is format the data correctly, peform the decryption, score the strings, and then sort our output. Similarly to the fixed-xor implementation, we will be accepting a hex value as a parameter. So, we need to xor each byte of the `hexVal` with the bits of the `possibleKey`. In one nested `for` loop, we can decrypt, score, and sort like so:

### Decryption Algorithm
```python
possible = string.printable

scores = []
for possibleKey in possible:
	decrypted = b''

	for byte in hexVal:
		decrypted += bytes([int(byte)^ord(possibleKey)])
			
	score = scoreString(decrypted)
	scores.append([decrypted, score])

scored = sorted(scores, key=itemgetter(1), reverse=True)
```
> This function employs the use of `itertools`, a useful python library for efficient looping. You can read up more about it on these [docs].

To review, we now have two functions that:
1. Analyzes strings and assigns a score of how likely it is to be English
2. Decrypts and sorts our output

Now, all we need to do is print our output. For now, our values are actually stored in a multi-dimensional list, with the decrypted value at index 0, and its score at index 1 for each list in the list of strings. It is also still in binary format, so we need to simply decode it in ascii characters.

### Printing Decoded Strings
```python
for decrypted in scoredStrings:
	print(decrypted[0].decode("ascii"))
```

With this, our script is ready to decrypt hex-encoded values that have been encrypted with a single-key. For more clarity on how to actually implement a full script you can take a look at it [here]:
```python
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
```

[docs]: https://docs.python.org/3/library/itertools.html
[here]: https://github.com/colton-gabertan/SecurityShepherdLabs/blob/XOR-Brute-Force/xorBruteForce.py
