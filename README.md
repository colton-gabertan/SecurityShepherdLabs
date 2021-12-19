# Session Management Challenge 2

**Instructions:**

Only an admin of the following sub-application can retrieve the result key to this challenge.

## Lab Walkthrough

This time around we are trying to get past some login credentials via poor session management. There's the login form and a reset password option, pretty standard for most web applications. Hence the prompt, let's try to see what happens when we login with the username *admin* and password *password*.

### Server Response
<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/Session-Management-Challenge-2/SesManagementChallenge2-0.gif">

In general when looking for vulnerabilities in web apps, it's always a good idea to get a feel for how it behaves, see if the default behavior itself presents any entry-points for us. As you can see, it looks like the username, "admin" was registered to that email address from the failed login attempt. Now that we have an email for the password reset, let's check out how this app chooses to reset passwords. 
