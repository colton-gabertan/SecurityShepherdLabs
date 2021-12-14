# Insecure Direct Object References

**Instructions:**

The result key to complete this lesson is stored in the administrators profile.

## Lab Walkthrough

As a precursor, make sure that you're viewing this challenge via BurpSuite's proxy so we can take advantage of the tool. Let's break down what we are presented with on the page for this challenge. There is a button for *Refresh your Profile* and it displays the results below it.

![image](https://user-images.githubusercontent.com/66766340/145984253-7b8b2963-eb94-4a8e-8c40-d52314438209.png)

Given this information, we need to take a look at the request we make to the server and see how it influences the response. My method is to hop back onto Burp and turn the intercept on. This will capture the packet and let us modify it before we send it out to the security shepherd server. Then, click the refresh button and observe our outgoing packet. 

Pay close attention to what we are actually sending to the web server. Experiment with changing things and see how it influences the responses. Based on the prompt, play around with some values in the outgoing request and see what is relevant to change. Once you're ready, hit send and see if what you did worked. 


