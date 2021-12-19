# Cross Site Request Forgery

**Instructions:**

The function used by an administrator to mark this lesson as complete for a user is initiated by the following GET request to this server, where 'exampleId' is a valid userId;
```
GET /root/grantComplete/csrfLesson?userId=exampleId 
```
To complete this lesson, use the Update User Image form below. The form accepts a URL that will be rendered as an HTML <img> on a separate part of the site that is only accessible to administrators. Knowing this, use the form to submit a malicious URL that will actually complete the request described above, replacing exampleId with your temp userId: 1908824607

## Lab Walkthrough

One thing to note about CSRF is that, in order for it to work, it requires that the user to run your request. This type of attack is very sneaky and takes advantage of tricking users into clicking on elements that they normally would. For this lesson, we need to update the img tag that an admin will be clicking on to review, in turn forcing them to make a malicious request without their knowledge. 

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

While the admin will see what looks like a broken image. The confusion tends to lead people to click on these; however, in this case his computer will run the GET request we intend for it to.

### Admin View:
![image](https://user-images.githubusercontent.com/66766340/146685060-6bb6aa86-740c-44c1-a2d9-cb5b32941da2.png)

