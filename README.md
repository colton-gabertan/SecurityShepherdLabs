# Insecure Cryptographic Storage Challenge 2

**Instructions:**

The result key has been encrypted to ensure that nobody can finish the challenge without knowing the secret key to decrypt it. The following form can be used to check if you have the correct result key.

## Lab Walkthrough

It seems all we are presented with for this challenge is a form that validates whether we have the result key or not. From the user interface, this looks extremely difficult. So, let's take a look at the page's source code in order to see if they left any important code out in the open. 

It looks like the developers left their crypto implementation out in the open.

```javascript
$("#leForm").submit(function(){
	// 2D Encryption
	var input = $("#resultKeyAttempt").val();
	theKey = "kpoisaijdieyjaf";
	var theAlphabet =   "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz";

	// Validate theKey:
	theKey = theKey.toUpperCase();
	var theKeysLength = theKey.length;
	var i;
	var adjustedKey = "";
	for(i = 0; i < theKeysLength; i ++)
	{
		var currentKeyChar = theAlphabet.indexOf(theKey.charAt(i));
		if(currentKeyChar < 0)
			continue;
		adjustedKey += theAlphabet.charAt(currentKeyChar);
	}
	theKey = adjustedKey;
	theKeysLength = theKey.length;

	// Transform input:
	var inputLength = input.length;
	var output = "";
	var theKeysCurrentIndex = 0;
	for(i = 0; i < inputLength; i ++)
	{
		var currentChar = input.charAt(i);
		var currentCharValue = theAlphabet.indexOf(currentChar);
		if(currentCharValue < 0)
		{
			output += currentChar;
			continue;
		}
		var lowercase = currentCharValue >= 26 ? true : false;
		currentCharValue += theAlphabet.indexOf(theKey.charAt(theKeysCurrentIndex));
		currentCharValue += 26;
		if(lowercase)
			currentCharValue = currentCharValue % 26 + 26;
		else
			currentCharValue %= 26;
		output += theAlphabet.charAt(currentCharValue);
		theKeysCurrentIndex =(theKeysCurrentIndex + 1) % theKeysLength;
	}
		
	// Check result for validity
	$("#resultDiv").hide("fast", function(){
		if(output == "DwsDagmwhziArpmogWaSmmckwhMoEsmgmxlivpDttfjbjdxqBwxbKbCwgwgUyam")
			$('#resultDiv').html("<p>Yeah, that's correct</p>");
		else
			$('#resultDiv').html("<p>No, that's not correct</p>");
		$("#resultDiv").show("slow");
	});
});
```

Let's reverse engineer this function a little bit to see if it's a widely recognized crypto implementation or if it's completely custom.

Here we have some statically defined values that will offer some hints.
```javascript
theKey = "kpoisaijdieyjaf";
var theAlphabet =   "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz";
```

theKey seems like it will work in conjunction with theAlphabet. Taking a look at the commented validation section, all it seems to do is make the key all uppercase, and ensure that each character is an english letter. Not much going on there. However, the "transform input" section is a bit more interesting. 

There is an empty output variable that gets mutated using index values of the alphabet and the key. Some interesting key points in this code snippet are the use of the modulo (%) and its implementation with the key and alphabet:
``` javascript
if(lowercase)
	currentCharValue = currentCharValue % 26 + 26;
else
	currentCharValue %= 26;
output += theAlphabet.charAt(currentCharValue);
theKeysCurrentIndex =(theKeysCurrentIndex + 1) % theKeysLength;
```

The modulo operator is used to perform integer division and return the remainder of the operation, making it a useful operator to implement a wrapping function within code. Seeing that there are 26 letters in the alphabet, this function seems to wrap a lot, as if the values could be represented by a table. 

One cryptographic algorithm that uses a key and wrapping is called the Vigenere Cipher. 

### Vigenere Cipher
[![Vigenere Cipher](https://github.com/colton-gabertan/SecurityShepherdLabs/blob/Insecure-Cryptographic-Storage-2/vigenere.gif)](http://www.youtube.com/watch?v=SkJcmCaHqS0)

*click on the gif for a quick explanation*

Further analyzing this function, we can spot an output validation section here:
```javascript
if(output == "DwsDagmwhziArpmogWaSmmckwhMoEsmgmxlivpDttfjbjdxqBwxbKbCwgwgUyam")
	$('#resultDiv').html("<p>Yeah, that's correct</p>");
```
So, to take inventory of what we know, we have:
1. the key
2. the cipher
3. output validation string

Let's hop back onto CyberChef and see if we can crack this Vigenere implementation.

### Cracking Vigenere Cipher w/ CyberChef
![image](https://user-images.githubusercontent.com/66766340/147610379-45ca6212-d0ee-42fd-a7ff-48b07926892f.png)

As you can see, the developers left their crypto implementations out in the open. This allowed us to extract the necessary information to crack their encrytion. It is also generally bad practice to have a validation such as this one, as it makes it extremely easy to bypass certain securities in other types of user input forms. For example, if passwords were validated in this manner, it would be easy to recover the plaintexts. 
