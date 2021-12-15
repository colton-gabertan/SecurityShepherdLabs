# Insecure Direct Object References Challenge 1

**Instructions:**

The result key for this challenge is stored in the private message for a user that is not listed below...

## Lab Walkthrough

Similar to the IDOR introduction, we need to find some way to influence the data that we submit to the web form. My approach did not need BurpSuite as some basic reconnaissance of the page's source code can reveal a little bit about how the developer implemented the method that actually accesses the data from the backend. 

To view a page's source code you can right click on the page or a specific element and select *inspect element*, or a little shortcut for chromium-based browsers is to hit Ctrl+Shift+I. A good place to start would be at the form we are submitting.

### Inspecting the web form
<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/IDOR-Challenge-1/IDORchallenge1.gif">

### Web form structure
![image](https://user-images.githubusercontent.com/66766340/146166359-a26bb5b0-27a5-43c4-83c7-af228ad97901.png)

So, from a very high level perspective, let's break down how this web form is functioning. We can see those **option** tags, within them containing the name of the user's profiles. However, notice how there is a value inside of the tag correlating with these names. In reference to the prompt, how can we manipulate something about these tags and submit requests that we aren't supposed to?

Let's look for a pattern in those values, we can see it incrementing in odd order: 1, 3, 5, 7, 9...

If the form is definitely displaying results for the odd numbered values, why not try submitting an option with a value of what comes next in the list, 11.



