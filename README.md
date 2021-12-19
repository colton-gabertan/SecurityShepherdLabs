# Cross Site Request Forgery

**Instructions:**

The function used by an administrator to mark this lesson as complete for a user is initiated by the following GET request to this server, where 'exampleId' is a valid userId;
```
GET /root/grantComplete/csrfLesson?userId=exampleId 
```
To complete this lesson, use the Update User Image form below. The form accepts an URL that will be rendered as an HTML <img> on a separate part of the site that is only accessible to administrators. Knowing this, use the form to submit a malicious URL that will actually complete the request described above, replacing exampleId with your temp userId: 1908824607

## Lab Walkthrough
