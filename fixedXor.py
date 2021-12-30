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
