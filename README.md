# SQL Injection 3

**Instructions:**

To complete this challenge, you must exploit a SQL injection issue in the following sub application to acquire the credit card number from one of the customers that has a customer name of Mary Martin. Mary's credit card number is the result key to this challenge.

## Lab Walkthrough

In this challenge, we are now asked to target a specific user, rather than performing a full on table dump. This means that we will have to modify the search query in our favor, which will involve a bit of educated guess work and some testing. First things first, let's see if we can trigger an error for a clue as to how we can escape the user input string and start messing with the query.

### Probing the Filter
![image](https://user-images.githubusercontent.com/66766340/147537974-7f04d79c-cd36-431e-95b7-925471bf8ddf.png)

Luckily, it doesn't look like this filter is as beefy as the last one; however, the difficulty in performing this injection is guessing the names of the parameters within the search query. By default, looking at the web form, it seems it just dumps general information about the users entered, rather than a specific field, so we can infer that the query looks a bit like:
```MySQL
SELECT * FROM customers WHERE customer_name='';
```

This query is alright for dumping general information about a given user; however, we are specifically looking for Mary Martin's credit card number. A query that might return that information may be:
```MySQL
SELECT credit_card_number FROM customers WHERE customer_name='Mary Martin';
```

So essentially, instead of accessing general information that is publicly available, we need to modify the original search query so that it includes the fields we want to access. This is where the UNION operator comes in handy. Syntatically, this allows us to combine search queries in SQL. The full query after our injection should look like:
```MySQL
SELECT * FROM customers WHERE customer_name='Mary Martin' UNION SELECT credit_card_number FROM customers WHERE customer_name='Mary Martin';
```

Now that we know what our query needs to be, it is a matter of defeating whatever filters are implemented as well as getting the field names correct. It is good practice in software engineering to give things names that make sense, so I'd maybe test the injection using camelCase, snake_case, or simply lowercase.

Knowing that we can easily close the string with a single quote, our actual injection should look like:
```MySQL
Mary Martin' UNION SELECT creditcardnumber FROM customers WHERE customername = 'Mary Martin;--   
```

I included Mary Martin's name in the first part in order to satisfy the field's filter, closing the first string with the single quote. I then inserted our UNION clause, and experimented with what the developers may have named the fields. From there, I delimited the line syntatically with ";" and commented out the last quote in order to end the search query.

### Injecting the UNION Clause
<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/SQLI-3/SQLI3.gif">

--

### Developer Considerations

Although it was somewhat well thought out in how they restriced the information shown in the default search query, they still left sensitive information accessible in a regular search query from this form. When managing databases, it is important to be able to really restrict the sensitive information to only the people who should be seeing it. Handle sensitive data accordingly and make sure to guard it closely in order to protect not only the user, but also the company/ organization that hosts the web application.
