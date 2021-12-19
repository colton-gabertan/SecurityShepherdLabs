# Session Management Challenge 3

**Instructions:**

Only an admin of the following sub-application can retrieve the result key to this challenge. You have been granted user privileges because the admins need somebody to boss around.

## Lab Walkthrough

Maybe thanks to how easy the last challenge was, the developers decided to update their login features. However, let's test it further and see if the new implementation can hold its own. Approaching it exactly as we did before, let's test if there is a user called "admin".

### New Error Message
![image](https://user-images.githubusercontent.com/66766340/146683381-ddcf21bb-a97e-4103-be40-f6140335305d.png)

Good, it looks like they stopped showing the admin's email address, but they still left us a hint that "admin" is still a registered user. Next, let's check out the *Toggle user functions* request and see what information we can pull from the client-server exchange. I'll use the password: "password" and see how it behaves.

### Client-Server Traffic: Change Password
![image](https://user-images.githubusercontent.com/66766340/146683508-6b3269c1-4a5a-40c1-8115-9607f8bd9141.png)

Alright, also a bit better. Just as another security consideration, never send the new password value in the clear, as anyone listening in will pretty easily steal that bit of information. Furthermore, taking notice to the cookies, we can see this field:
```
current=WjNWbGMzUXhNZz09
```

As this request is to reset the password, it is safe to assume that "current" refers to which user's password we are trying to reset. One thing they got right this time is obfuscating the value, but there surely must be a way to break that crypto. For this one, I recommend simply taking advantage of Burp's decoder.

*Side note: just to start gaining more familiarity with encodings/ encryptions, base64 **generally** ends with an "=" or "=="; however, it is not always the case. Some other key factors to look out for is if the length is a multiple of 4, and if it is using only specific characters that base64 implements in its algorithm.*

### Decoding the User Cookie
![image](https://user-images.githubusercontent.com/66766340/146683802-1886e599-dbfe-48ec-adb6-9ab71b7a80b5.png)

One run through base64 and we find a more familiar version of it, a second time, and we've exposed the developer's weak implementation of crypto. As you can see, we've not only found our decoded value, but we've figured out how to re-encode a different one for tampering purposes. Seeing that we now know how to reverse the crypto, let's encode our new value:
```
admin => YWRtaW4= => WVdSdGFXND0=
```

Now, let's plug it into the current field and see if we can reset admin's password. 

### Forged Session Attack Results
![image](https://user-images.githubusercontent.com/66766340/146683938-71d3ed6e-fe56-45cd-be30-8c60f32a52c1.png)

Based on the response, it looks like we successfully reset admin's password to our own. All that's left is to sign in and grab that key!



