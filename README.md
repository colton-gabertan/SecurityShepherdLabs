# SQL Injection

**Instructions:**

Exploit the SQL Injection flaw in the following example to retrieve all of the rows in the table. The lesson's solution key will be found in one of these rows! The results will be posted beneath the search form.

## Lab Walkthrough

These labs do assume some basic understanding of SQL. If it is your first time completely working with SQL, I recommend checking out these materials:
* [Free Khan Academy on SQL]
* [Free SQL Udemy Course]

For our labs, we will mostly be looking into how we can take advantage of the search query specifically. These web pages make requests to its backend which is in SQL, so if we can achieve remote code execution via sqli, we will mostly be using it to expose data that we normally shouldn't be allowed to see. However, the capability of SQLI spans much further than that.

Let's take a look at the structure of a search query:
```MySQL
SELECT field_list FROM table WHERE field=''
```

Web pages prompt users in a way where their input will be a valid field value for whatever the server must lookup for them. Let's take a look at our lab's input field and make some assumptions about the search query here.

### Web Form for SQL Query Prompt
![image](https://user-images.githubusercontent.com/66766340/147068745-e4272513-0e82-4255-9371-1dc752edde3c.png)

Given that we're searching for general information of users based on the username, we can assume that the query looks something like:
```MySQL
SELECT * FROM users WHERE user_name=''
```

Building upon our skill set from the last challenge, we can picture the queries and try to inject some additonal SQL to get the server to display too much information. Given that this language sports logical operations, we can also take great advantage of boolean values.

I'll craft an injection that looks like:
```MySQL
'or'1=1
```

Appending this to the query it'll look like:
```MySQL
SELECT * FROM users WHERE user_name='''or'1=1'
```

Depending on how our input is handled, this query will simply display ALL of the user information, because of the True evaluation that results from the 1=1. The logical "or" operator ensures that only 1 needs to equal 1 in order for the results to be displayed. It won't matter if there is a valid user name input or not. The pre-pended (') is there to close out the initial query's string and let us add onto the query instead of the user's input string.

Let's see it it works!

### RCE from SQLI
![image](https://user-images.githubusercontent.com/66766340/147070269-2233209e-113a-4a57-b9fa-53d215c025d0.png)

As you can see, the entire table is displayed, when normally only one row of the table should be. This has lead to a data breach of the entire user base with one little input.

[Free Khan Academy on SQL]: https://www.khanacademy.org/computing/computer-programming/sql
[Free SQL Udemy Course]: https://www.udemy.com/course/introduction-to-databases-and-sql-querying/
