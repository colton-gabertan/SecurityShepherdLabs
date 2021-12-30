# Fixed XOR

**Description:**

This python script performs a fixed XOR operation on hex values. This is used as weak symmetric encryption algorithm.

## CTF Walkthrough

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
