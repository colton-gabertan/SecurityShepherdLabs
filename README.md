# Session Management Challenge 2

**Instructions:**

Only an admin of the following sub-application can retrieve the result key to this challenge. You have been granted user privileges because the admins need somebody to boss around.

## Lab Walkthrough

Maybe thanks to how easy the last challenge was, the developers decided to update their login features. However, let's test it further and see if the new implementation can hold its own. Approaching it exactly as we did before, let's test if there is a user called "admin".

### New Error Message
![image](https://user-images.githubusercontent.com/66766340/146683381-ddcf21bb-a97e-4103-be40-f6140335305d.png)

Good, it looks like they stopped showing the admin's email address, but they still left us a hint that "admin" is still a registered user. Next, let's check out the *Toggle user functions* request and see what information we can pull from the client-server exchange. I'll use the password: "password" and see how it behaves.

### Client-Server Traffic: Change Password
![image](https://user-images.githubusercontent.com/66766340/146683508-6b3269c1-4a5a-40c1-8115-9607f8bd9141.png)

Alright, also a bit better. Just as another security consideration, never send the new password value in the clear, as anyone listening in will pretty easily steal that bit of information. Furthermore, taking notice to the cookies, 
