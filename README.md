# Fixed XOR

**Description:**

This python script performs a fixed XOR operation on hex values. This is used as weak symmetric encryption algorithm.

## fixedXor.py 

Before we get into coding the script, you must first understand how the xor operation works on a set of binary digits. "XOR" (^) stands for "exclusive or", meaning in order for this operation to evaluate to true, both of the operands must be different. So, only a 1 ^ 0 or a 0 ^ 1 will evaluate to 1. 1 ^ 1 and 0 ^ 0 both evaluate to 0.

Given 01101001 and 00111010 we can xor these two values like so: \
*starting from the right-most bit going to the left*

### Fixed XOR as Encryption & Decryption
```
01101001 - value 1      01010011 - encrypted              01010011 - encrypted
00111010 - value 2      00111010 - value 2                01101001 - value 1
--------                --------                          --------
01010011 - encrypted    01101001 - value 1 (decrypted)    00111010 - value 2 (decrypted) 
```

Say value 1 and value 2 were hex-encoded plaintext messages, if we xor them, we get an encrypted hex string. But taking the encrypted hex string and xor'ing it by the original values essentially decrypts the messages. This is why it is an easy crypto to break. However, the focus is on writing a script that performs this operation.

One thing to note is that we need our values to be of the same length in binary. Let's start by creating a function that we will use to set a fixed length for our binary values in order to perform a successful xor.
```python
# getLength: finds final length for binary values
# parameters: bin1, bin2
# return: length to match binary values
def getLength(bin1, bin2):

	length = len(bin1) if len(bin1) > len(bin2) else len(bin2)

	return length
```

Personally, to allow for more flexibility of the script, I want it to accept cmd-line args so we can xor any two hex values, rather than hard-coding it into our script. In the main function, I scan the user input and convert the expected hex strings into binary integers.
```python
userInput1 = str(sys.argv[1])
userInput2 = str(sys.argv[2])

binVal1 = bin(int(userInput1, 16))[2:]
binVal2 = bin(int(userInput2, 16))[2:]
```

To pick apart how I get from a hex *string* to a binary *integer*, the function int() accepts two arguments. It accepts, first the value to be casted and then the base of the number. Hexadecimal has a base of 16. So, int(hexString, 16) effectively turns a data-type str, hexString, into a hexadecimal numerical data type, int. Once we have our hex string as a hex int, we must convert it to binary with the bin() function. My only gripe with the bin() function is that it always pre-pends the return value with "0b", so in order to just get the binary, we have to slice off the "0b" with [2:].

From here, our script can turn hex strings into binary digits, and it can determine a length to set our binary digits up for a proper xor. Usually when working with unsigned binary values of different lengths, we perform a zero-fill until they are the same length. Luckily, python has a function that does just that, zfill(). We will use this function to complete the formatting of our data and move onto the xor operation. 

I decided to zfill the binary values in the same function that will xor them.
```python
def xorVals(length, bin1, bin2):

	bin1.zfill(length)
	bin2.zfill(length)
```

So, we now have the binary digits and they are the same size, ready for the xor operation. In python, it is particularly easy to do this by zipping the values together and xor'ing each bit using a list comprehension. It can be done in one line like so:
``` python
xor = [int(x)^int(y) for x,y in zip(bin1, bin2)]
```

This will return a list of the xor'ed bits. If we were to print it as is, it would look like:
``` python
[1,0,1,0,0...]
```
So, to help with the final formatting, we can convert it back to a str data type, and from there we can convert it from a binary str to a hex int, yielding us the encrypted hex value. So, to get the hex value:
```python
xorStr = "".join([str(bits) for bits in xor])
finalXor = hex(int(xorStr, 2))[2:]
```

Using list comprehension once again, we simply append each bit, but casted as a str to an empty string, leaving us with the binary str. From there, we cast it back to a binary digit with the int(binaryStr, 2) and convert it back to hex(), slicing off the pre-pended "0x" from the hex() function.

And with that, we've performed the operation. By the xor encryption scheme, the same operation, but performed with the encrypted value and original ones will essentially decrypt the messages. This is why I wrote the script to take cmd-line args, instead of hard-coded values.

To glue all of this logic together, you can take a look at the full script [here]:
``` python
#!/usr/bin/env python3

### imports for program
import sys

##################################################################################
### function implementations
##################################################################################

# getLength: finds final length for binary values
# parameters: bin1, bin2
# return: length to match binary values
def getLength(bin1, bin2):

	length = len(bin1) if len(bin1) > len(bin2) else len(bin2)

	return length

# xorVals: formats binary values and xor's each bit
# parameters: length, bin1, bin2
# return: returns hex string, resulting from xor operation
def xorVals(length, bin1, bin2):

	bin1.zfill(length)
	bin2.zfill(length)

	xor = [int(x)^int(y) for x,y in zip(bin1, bin2)]
	xorStr = "".join([str(bits) for bits in xor])
	finalXor = hex(int(xorStr, 2))[2:]

	return finalXor

##################################################################################
### Main entry point for program
##################################################################################

# main: reads cmd-line args and xor's hex strings
#       usage: ./fixedXor.py <hex value 1> <hex value 2>
# parameters: n/a
# return: prints xor'd hex strings as a hex value
def main():

	userInput1 = str(sys.argv[1])
	userInput2 = str(sys.argv[2])

	binVal1 = bin(int(userInput1, 16))[2:]
	binVal2 = bin(int(userInput2, 16))[2:]

	length = getLength(binVal1, binVal2)
	xord = xorVals(length, binVal1, binVal2)

	print(xord)

if __name__ == '__main__':

	main()

```

[here]: https://github.com/colton-gabertan/SecurityShepherdLabs/blob/Fixed-XOR/fixedXor.py
