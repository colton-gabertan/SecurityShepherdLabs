# Cross Site Scripting 2

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

Similar to the last challenge, we know that this filter will be different. So let's probe it as we did last time. Since the page presents us with an input field and a button, I'd like to test out the third generic input:
```HTML
<INPUT TYPE="BUTTON" ONCLICK="alert('XSS')"/>
```

Submit it and let's try to see how the filter is implemented.

### Probing XSS Filter
![image](https://user-images.githubusercontent.com/66766340/147013707-b8a9450f-c063-44a0-8091-ecf965df10f3.png)

It actually looks like it accepted our INPUT tag and started interpreting a lot of it; however, it's pretty clear that if the string "onclick" is in there, it will guard against it. Interestingly though, it will get interpreted as "on.ick". It seems that it will leave the "on" part, and only filter the "cl" leaving us with some options. Now that we know that most of our tag gets interpreted the next step is to see if we can beat that substring filter. 

If you're not too familiar with web development, I recommend reading up a little bit about [events]. Events are javascript triggers that run some code based on some actions or states of the page. "Onclick" is only one of these events, so, are there any other events we can try out to bypass the filter that we know definitely defeats onclick? Try to pick one that is actually appropriate for the action.

I'll try ONSUBMIT:
```HTML
<INPUT TYPE="BUTTON" ONSUBMIT="alert('XSS')"/>
```

### Adjusting Tag and Event handler
![image](https://user-images.githubusercontent.com/66766340/147014123-ba77b33a-c4c5-4211-b98c-1cd28587b295.png)

As you can see, this filter was still pretty weak; but, this does showcase how deeply we can filter inputs. We've seen that we can implement it to take out full tags/ strings, and even substrings. The only limit is how accessable/ flexible you'd like the input field to be for your actual users while having appropriate filters on them to stop malicious ones. Keep in mind that over-filtering can potentially affect the performance of your application, so it's important to find that sweet spot.

I'll also encourage you to see if any other event tags can beat this filter!

[events]: https://www.w3schools.com/js/js_events.asp
