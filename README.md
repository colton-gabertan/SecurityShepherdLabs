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

Now that we've exploited a couple of more commonplace web forms, this one is different in that it asks for a URL, meaning it will implement our input into an "a" tag. When developing with HTML, "a" tags are typically used to place links on the webpage. Luckily for us, it has a lot of functionality to explore. You can read more about them [here].

The new prompt for the challenge also lets us know how the filter is implemeted. The developers decided to escape certain characters in order to not let some malicious input get interpreted by their server. This sort of filter is a pretty decent implementation; however, the downside is that you have to test all possible cases in order for it to be considered not vulnerable. 

Let's start by probing this form with an actual URL and some XSS input that we've used before to observe the filter.
I'll use an onclick event handler:
```HTML
https://google.com onclick="alert('xss')"
```

### Observing the New Filter
![image](https://user-images.githubusercontent.com/66766340/147059997-828d2784-d074-405e-ab4c-0efdd3ce2076.png)

As we suspected, some mandatory syntatical characters get escaped; however, one other issue is that our event handler was a part of the string. But, some more vital information is that the event handler does not get escaped if it's within the input string. So, the first step would be to figure out how we can close that string and inject into the tag, rather than having our attribute in the displayed input field.

Let's try manually closing the string ourselves with a double quote (") and proceeding from there:
```HTML
https://google.com" onclick="alert('xss')"
```

### Closing the Input String First
![image](https://user-images.githubusercontent.com/66766340/147060713-47750181-6999-4ee3-8926-3bc47b299576.png)

Perfect, it seems we've figured out how to jump into the tag, so the next challenge is to figure out what the developers have forgotten to escape and how to use a different attribute to run our malicious javascript. Furthermore, after an "=" is detected in a tag, it adds double quotes after it automatically.

As I stated earlier, we are lucky that we're working with an "a" tag, because it supports a wide range of attributes. Let's take a look at the last generic XSS input, specifically the src attribute as it is supported by the "a" tag.
```HTML
SRC="javascript:alert('XSS');"
```

This is an interesting use of the javascript [void operator]. Typically it's used during the development cycle as a placeholder in tags such as the "a" one. However, we can leverage it to execute different code as well.

Given that we know that any of the event handlers starting with "on" are escaped, and after we input an "=" into the tag, quotes are added automatically, we can adjust our XSS attempt accordingly:
```HTML
https://google.com" src=javascript:alert('xss');
```

### Beating the Filter
![image](https://user-images.githubusercontent.com/66766340/147062318-2ddc40d2-ff23-491c-a974-d08e3a96c089.png)

Just like that, we've tested the filter further, exposing a test case that the developers had missed!

[here]: https://www.w3schools.com/tags/tag_a.asp
[void operator]: https://www.w3schools.com/jsref/jsref_operators.asp
