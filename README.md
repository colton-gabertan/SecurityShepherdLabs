# SQL Injection 1

**Instructions:**

To complete this challenge, you must exploit SQL injection flaw in the following form to find the result key.

## Lab Walkthrough

One crucial aspect in detecting if a web application even uses SQL in its stack is to see if we can trigger an error message. Usually meant for programmers, error messages are meant to aid in the development process; however, if the application allows error messages to be displayed to the user, it can offer up clues as to how its filters work as well. Similar to how we probed the forms last week, our goal is to now see if we can get any error messages. The information we can gather from the front-end isn't as valuable as our goal is to inject code into the back end.

Essentially, input tends to be a string. Almost universally, strings are always in single-quotes (') or double-quotes ("). Since we're working almost exclusively with queries, a good way to start is to figure out if the application is programmed to accept strings that are in either one of the two quotes. I like to start with the single-quote.

### Single-Quote Test
![image](https://user-images.githubusercontent.com/66766340/147097975-f1efc420-d787-4649-bba7-8e4eabaa6f3d.png)

Alright, it looks like it accepted it in the input, meaning we probably didn't close the string. Let's try the double-quote next.

### Double-Quote Test
![image](https://user-images.githubusercontent.com/66766340/147098079-237fb9d2-cfbc-4dff-9cf6-2fed0c25ee10.png)

That's what we're looking for! Not only did it allow us to figure out how to close the string, but also which version of SQL the web app uses. In this case, it's using MySQL. For more advanced SQLI, knowing which type of SQL you're working with can greatly reduce the amount of time spent trying to test for vulnerabilities.

Now that we know this query looks a bit like:
```MySQL
SELECT * FROM customers WHERE customer_id=""
```

Let's add onto the query, similarly to the last challenge:
```MySQL
"or"1=1
```

We'll inject this into the search query and see if we can get another table to dump.

### "or"1=1
![image](https://user-images.githubusercontent.com/66766340/147098792-c6b28dbe-20bf-4f3f-8554-152470f13ecb.png)

As you can see, SQLI will be very picky and it ultimately depends on how the application was programmed. This makes these types of filters a bit more tricky to figure out, so I encourage you to continue playing around with the syntax, experimenting, and ultimately dumping those tables to collect those flags!
