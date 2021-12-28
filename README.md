# SQL Injection 3

**Instructions:**

To complete this challenge, you must exploit a SQL injection issue in the following sub application to acquire the credit card number from one of the customers that has a customer name of Mary Martin. Mary's credit card number is the result key to this challenge.

## Lab Walkthrough

In this challenge, we are now asked to target a specific user, rather than performing a full on table dump. This means that we will have to modify the search query in our favor, which will involve a bit of educated guess work and some testing. First things first, let's see if we can trigger an error for a clue as to how we can escape the user input string and start messing with the query.

### Probing the Filter
![image](https://user-images.githubusercontent.com/66766340/147537974-7f04d79c-cd36-431e-95b7-925471bf8ddf.png)

Luckily, it doesn't look like this filter is as beefy as the last one; however, the difficulty in performing this injection is guessing the names of the parameters within the search query. By default, looking at the web form, it seems it just dumps general information about the users entered, rather than a specific field, so we can infer that the query looks a bit like:
```MySQL
SELECT * FROM customers WHERE customer_name=''
```

