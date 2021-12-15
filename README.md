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



