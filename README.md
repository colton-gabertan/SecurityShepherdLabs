# Cross Site Request Forgery

**Instructions:**

The function used by an administrator to mark this lesson as complete for a user is initiated by the following GET request to this server, where 'exampleId' is a valid userId;
```
GET /root/grantComplete/csrfLesson?userId=exampleId 
```
To complete this lesson, use the Update User Image form below. The form accepts a URL that will be rendered as an HTML <img> on a separate part of the site that is only accessible to administrators. Knowing this, use the form to submit a malicious URL that will actually complete the request described above, replacing exampleId with your temp userId: 1908824607

## Lab Walkthrough

One thing to note about CSRF is that, in order for it to work, it requires the user to run your request. This type of attack is very sneaky and takes advantage of tricking users into clicking on elements that they normally would. For this lesson, we need to update the img tag that an admin will be clicking on to review, in turn forcing them to make a malicious request without their knowledge. 

Essentially, we are trying to set the src inside of an image tag to make a HTTP GET request to a malicious domain.

Modify this challenge's url and update the path, making sure that we are using the userId provided. After doing so, we can force the server to complete the lesson for us, but only *after* an admin runs the request by clicking on the img.

### Modified URL
```
https://security.codepath.com/root/grantComplete/csrfLesson?userId=1908824607
```

In turn, on the admin's HTML part of the page, the img tag will look like:
``` HTML
<img src="https://security.codepath.com/root/grantComplete/csrfLesson?userId=1908824607">
```

While the admin will see what looks like a broken image. The confusion tends to lead people to click on these links; however, in this case his computer will run the GET request we intend for it to.

### Admin View:
![image](https://user-images.githubusercontent.com/66766340/146685060-6bb6aa86-740c-44c1-a2d9-cb5b32941da2.png)

Hiding malicious requests in images and things of this nature is commonplace in phishing attacks, wherein a threat actor will hide either code or url's in emails for users to click on. This can result in them downloading malware, among other things.

The next challenges in this week's labs do require you to have someone manually run your CSRF attack. So I suggest partnering up and studying up about how to take advantage of a server to host your malicious code. It is possible to do them solo; however, I will leave it up to your disgression as to how to accomplish that if you would like to do so.

---

### Web Application Development Considerations
In general, one good way to prevent an attack such as this one is to really control where these form submissions are sent. Make sure to sanitize input, ensuring that it is appropriate for the form. Strip it of anything resembling the code of your tech stack and make sure that nothing can really go through. There are secure frameworks, and taking advantage of them is wise, as the filtering functions are tried and true.

