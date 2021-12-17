# Session Management Challenge 1

**Instructions:**

Only administrators of the following sub-application can retrieve the result key.

## Lab Walkthrough

Now that we've established a general method to completing these session-based attacks, this challenge presents us with a cookie that is used for authentication. We must trick the server into believing that we are accessing the feature as an admin. Let's intercept that request and see what we can work with.

### Administrator Only Button Request
![image](https://user-images.githubusercontent.com/66766340/146511904-ac5818a7-c51c-476e-b24d-259046783f9c.png)

This time around, at least the cookie values are encoded. However, Burpsuite has a neat little feature called the decoder. We can highlight the value we want to decode, right-click and select *send to decoder*. Recognizing which method was used to decode values is a matter of experience and exposure, but in general, base64 can be recognized as having "=" at the end of the digest. Let's decode the checksum value and take a look at what it translates to.

### Decoding Checksum Value
<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/Session-Management-Challenge-1/SessionManagementChallenge1.gif">

Thanks to the decoder, we can see that the decoded value is:
```
userRole=user
```
Within the same tab, the decoder also allows us to encode values. Now that we know how to syntatically send this data, lets try to pose as an admin, changing the value accordingly:
```
userRole=admin
```
Then we need to re-encode it back to base64 to fit the cookie format, yielding:
```
dXNlclJvbGU9YWRtaW4=
```
Let's hop back onto the intercepted packet, tamper with the request, and access the application with admin privileges.

### Web Response Page
![image](https://user-images.githubusercontent.com/66766340/146513583-25745ac3-375a-4e9e-a1f9-296eb16494b7.png)

Oops, it looks like we got caught trying to hack this app. This queues us in to believe that we fell victim to the application's honeypot, which is a fake portion designed to let us observe the actions of a malicious user. The session cookie in this case was set up as bait. It seems that this page is more sophisticated than we think, but some attention to detail may net us some redemption.

Pay close attention to the way the prompt was worded. "Only **administrators**" and "**Administrator Only Button**". Let's try to encode the string "userRole=administrator" to base64 and re-run our attack.

### Encoding "userRole=administrator"
```
userRole=administrator => dXNlclJvbGU9YWRtaW5pc3RyYXRvcg==
```

And success! We've bypassed the authentication, but triggered the honeypot alert in the process. We're lucky that this honeypot stopped there, very good ones can even launch counter-attacks, alert the security team, and blacklist client servers. That is a little teaser for the optional section of this course!
