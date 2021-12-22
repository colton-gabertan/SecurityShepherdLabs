# Cross Site Scripting 4

**Instructions:**

Generic XSS injections:
```HTML
<SCRIPT>alert('XSS')</SCRIPT>
<IMG SRC="#" ONERROR="alert('XSS')"/>
<INPUT TYPE="BUTTON" ONCLICK="alert('XSS')"/>
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
```

Demonstrate a XSS vulnerability in the following form by executing a JavaScript alert command. The developers had heard that escaping is a better way of fixing XSS issues but they were not totally clear on how to implement it.

## Lab Walkthrough

Now that we've exploited a couple of more commonplace web forms, this one is different in that it asks for a URL, meaning it will implement our input into an "a" tag. When developing with HTML, "a" tags are typically used to place links on the webpage. Lucily for us, it has a lot of functionality to explore. You can read more about them [here].

[here]: https://www.w3schools.com/tags/tag_a.asp

The new prompt for the challenge also lets us know how the filter is implemeted. The developers decided to escape certain characters in order to not let some malicious input get interpreted by their server. This sort of filter is a pretty decent implementation; however, the downside is that you have to test all possible cases in order for it to be considered not vulnerable. 

Let's start by probing this form with an actual URL and some XSS input that we've used before to observe the filter.
I'll use an onclick event handler:
```HTML
https://google.com onclick="alert('xss')"
```

### Observing the New Filter
![image](https://user-images.githubusercontent.com/66766340/147059997-828d2784-d074-405e-ab4c-0efdd3ce2076.png)

As we suspected, some mandatory syntatical characters get escaped; however, one other issue is that our event handler was a part of the string. So, the first step would be to figure out we can close that string and inject into the tag, rather than having our attribute in the displayed input field.

