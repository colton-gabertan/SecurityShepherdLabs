# Cross Site Scripting

**Instructions:**

Generic XSS injections:
```HTML
<SCRIPT>alert('XSS')</SCRIPT>
<IMG SRC="#" ONERROR="alert('XSS')"/>
<INPUT TYPE="BUTTON" ONCLICK="alert('XSS')"/>
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
```

The following search box outputs untrusted data without any validation or escaping. Get an alert box to execute through this function to show that there is an XSS vulnerability present.

## Lab Walkthrough

In my opinion, this is where we begin to exercise our creativity and demonstrate a bit more code knowledge. The first line of defense against Cross Site Scripting (XSS) is filtering inputs on the web application. In a more practical sense, it wouldn't be filtered right at the front-end, as that would offer hints as to how to defeat these filters; however, for the purposes of lab, we will be inspecting the page a lot to try and experiment with XSS inputs.

Essentially, when we inject this code, the web server will interpret it as its own, allowing attackers the full power of HTML and javascript to do whatever they want with the page. This is why XSS is so dangerous. Attackers can do things ranging from defacing the website, hijack user sessions by abusing the cookies, or even steal accounts and private data with one wrong click from the user.

We're going to try the first generic injection:
``` HTML
<SCRIPT>alert('XSS')</SCRIPT>
```

### Injecting the XSS line
<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/Cross-Site-Scripting/XSS0.gif">

As the server sees this input, it will recognize the SCRIPT tag and process it as if it were its own source code. Since within the SCRIPT tag, which allows us to embed javascript directly in the HTML, we have an alert; upon interpreting the code, the page will be met with a pop up once the form is submitted. Using a javascript alert() is an indication that we can potentially run an XSS, but for us, as testers, it lets us know *how* the page may be injectable. In this case, *any* javascript between the SCRIPT tags is fair game and will run.
