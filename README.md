# SQL Injection 2

**Instructions:**

To complete this challenge, you must exploit SQL injection flaw in the following form to find the result key.

## Lab Walkthrough

Sometimes, there are layers to the filters. In the case of this challenge, we are asked for a valid email address. It may seem simple to validate the structure of an email adress i.e. something like "foo@bar.com" could satisfy the conditions; however, due to the range of what can be considered a valid email address universally, we are given some lee-way to bypass this filter.

Let's start by testing out the filter, seeing if we can get an error message to be issued. Keep in mind that the first layer of the filter looks at the user's input, trying to validate if there is an email in the string. I'll start with a single-quote, followed by a dummy email *foo@bar.com*.
```
'foo@bar.com
```

### Triggering Error for Clues
![image](https://user-images.githubusercontent.com/66766340/147100896-b4da3f75-519d-40de-b2cb-87f85ecae3c5.png)

So, we've found out a couple of things. As long as there is a string that follows the syntax of a valid email, anything else we put in has the possibility of getting interpreted as a query by the back end. With this information let's craft a new query:
```MySQL
'or'1=1foo@bar.com
```

This new input string both tells the backend to dump the table and satisfies the email validation filter.

### Adding to Query, Following Email Condition
![image](https://user-images.githubusercontent.com/66766340/147101350-b41f8cf8-f323-4eba-8c08-40fd255ec854.png)

And just like that, because of poor email validation, we are able to manipulate the search query and dump the table! This one goes to show that filtering may seem like common sense; however, it is still important to run all possibilites when testing. Always consider how your filters may be broken and address ways that they may be improved.
