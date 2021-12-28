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

theKey seems like it will work in conjunction with theAlphabet. Taking a look at the commented validation section, all it seems to do is make the key all uppercase, and ensure that each character is an english letter. Not much going on there.


