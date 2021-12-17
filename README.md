# Broken Session Management

**Instructions:**

This lesson implements bad session management. Investigate the following function to see if you trick the server into thinking you have already completed this lesson to retrieve the result key.

## Lab Walkthrough

This week we'll begin to start abusing broken authentication and session management. When we visit websites, the web server needs a way to identify the machine that is interacting with its app. Session cookies are assigned to the client machine whenever a session is opened i.e. whenever you visit the site or login. There are many uses to these session cookies such as saving the state of the page or helping pre-load frequently visited pages for better performance. However, when used for authentication and other sensitive services, the developer must be extra careful to not present an exploitable vulnerability.

Because of the nature of cookies, we need to observe this application's behavior via Burpsuite. On this challenge we are simply presented with a *Complete This Lesson* button and we need to tamper with our request to trick the server into thinking we've actually completed the lesson.

I decided to intercept the request, check out the information we are actually sending to the server, modify the LessonComplete field and forward the it.

### Intercept, Tamper, Forward
<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/Broken-Session-Management/BrokenSessionManagement.gif">
