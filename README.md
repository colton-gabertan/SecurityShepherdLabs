# SQL Injection

**Instructions:**

Exploit the SQL Injection flaw in the following example to retrieve all of the rows in the table. The lesson's solution key will be found in one of these rows! The results will be posted beneath the search form.

## Lab Walkthrough

These labs do assume some basic understanding of SQL. If it is your first time completely working with SQL, I recommend checking out these materials:
* [Free Khan Academy on SQL]
* [Free SQL Udemy Course]

For our labs, we will mostly be looking into how we can take advantage of the search query specifically. These web pages make requests to its backend which is in SQL, so if we can achieve remote code execution via sqli, we will mostly be using it to expose data that we normally shouldn't be allowed to see.

Let's take a look at the structure of a search query:
```MySQL
SELECT field_list FROM table WHERE field=''
```

[Free Khan Academy on SQL]: https://www.khanacademy.org/computing/computer-programming/sql
[Free SQL Udemy Course]: https://www.udemy.com/course/introduction-to-databases-and-sql-querying/
