# HTTP Headers

**Instructions:**

Go to https://facebook.com. What is the Cache-Control header set to in the response? Enter as a comma-delimited list below. Order doesn't matter, and values are case insensitive.

## Lab Walkthrough

Although it isn't needed for these challenges, I would like to get you familiarized with how to use BurpSuite effectively. In this challenge, all it is asking is for you to extract some information from a http response header. 

So, fire up BurpSuite and make sure that you're viewing the browser via the proxy. It doesn't matter if you have set it up through Firefox with foxyproxy or are using the built-in chromium proxy. Personally, I like to just use the built-in one that is packaged with BurpSuite. Then, visit https://facebook.com as you would normally, and the traffic containing your request and the response to your request will show up in the http history tab.

From here, locate the data to be extracted from the response header and capture that flag!

### BurpSuite Demo
<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/HTTP-Headers/httpHeaders.gif">
