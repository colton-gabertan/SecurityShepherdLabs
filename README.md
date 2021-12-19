# Cross Site Scripting 1

**Instructions:**

Generic XSS injections:
```HTML
<SCRIPT>alert('XSS')</SCRIPT>
<IMG SRC="#" ONERROR="alert('XSS')"/>
<INPUT TYPE="BUTTON" ONCLICK="alert('XSS')"/>
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
```

Find a XSS vulnerability in the following form. It would appear that your input is being filtered!

## Lab Walkthrough

As I mentioned in the intro, the first line of defense agains XSS attacks is filtering input. Developers will take the strings and strip it of characters or substrings that would allow XSS; however, the filter is only as good as the developer.

As a starting-point, let's try rerunning the tag from the first task.

### Probing XSS filter
![image](https://user-images.githubusercontent.com/66766340/146686641-643eb62a-f45e-49a3-adaf-2e3b0d8e39e3.png)

So, it looks like it took the inner part of the SCRIPT tags, and simply recognized the javascript alert as a string. Let's take a closer look at the page by inspecting the error message.

### Source Code of Error Message
![image](https://user-images.githubusercontent.com/66766340/146686775-16897b2f-f25c-43cb-b07a-bdd921c5acd5.png)

Interesting, in this div, the SCRIPT tag looks like <scr.pt>. This, combined with the fact that the inside of our original SCRIPT tags was treated as a regular string can mean that this app filters out the SCRIPT tag. Luckily, there's ways to inject javascript within other tags. Take a look at the generic injections and test one out. 
