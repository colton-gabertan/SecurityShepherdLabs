# Cross Site Scripting 3

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

By now, you should be developing some sense as to how to probe the filter, so let's start to put more attention towards analyzing and defeating them! In the last challenge, it simply looked for "cl" and filtered out the substring, rendering the ONCLICK event guarded against. However, that still left the other event handlers useable.

Let's see how the filter works this time around:

### Probing Filter
![image](https://user-images.githubusercontent.com/66766340/147015259-a13a1e16-3ea9-498c-9310-0cf09ee9c48c.png)

Good, it looks our INPUT tag still gets interpreted; however, our entire event handler was filtered out this time. Let's mess around with the string and see if we can get it to run. Assuming that it is purely looking for event handlers, all of them are pre-pended with the substring: "on". I want to test if this filter is intelligent enough to see that and wipe out the entire string.

### Adjusted Input:
```HTML
<INPUT TYPE="BUTTON" ONONCLICK="alert('XSS')"/>

```

### Filter Behavior
![image](https://user-images.githubusercontent.com/66766340/147015483-ee91bdf9-a7a5-46df-8f73-b5d1032cd99e.png)

Nice, it looks like we're getting a bit warmer. It included the second "on", but filtered out the "click". So logically, this filter may work in a manner where if it detects the substring "on", it will look for "click" (or any other event handler tag) after, and if the substring "click" is present, it will filter it out. However, anything after the intial "on" is fair game, especially since it allowed a second instance of the substring "on". We can also assume that if we trigger the second part of the filter, it will likely leave and excess input in as well. 

So it looks like we'll simply have to play by the rules of the filter. But first, I'll draft up a bit of pseudo code to show it on a programatic level:

### Pseudocode of XSS Filter
```python
string substr1 = "on"
string substr2 = "click" # or a list of the event handlers (submit, load, etc...)

if substr1 in userInput:
  userInput = userInput[2:] # filters out "on" 
  
  if substr2 in userInput: # look for the attribute, delete next n characters where n = length of event tag
    userInput = userInput[:n]
```
*[Python3 slicing] to understand the psuedocode a bit better*


[Python3 slicing]: https://www.w3schools.com/python/python_strings_slicing.asp
