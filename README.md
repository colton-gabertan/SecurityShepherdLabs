# SQL Injection: Escaping

**Instructions:**

To complete this challenge, you must exploit SQL injection flaw in the following form to find the result key. The developer of this level has attempted to stop SQL Injection attacks by escaping apostrophes so the database interpreter will know not to pay attention to user submitted apostrophes.

## Lab Walkthrough

Given the prompt, it seems that the filter has caught onto our typical method of closing the input string, which allows us to modify the query directly. Just out of curiosity, I wanted to test if a single- or double-quote would even trigger an error. 

### Testing the Filter
<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/SQLI-Escaping/SQLIescaping.gif">

Interestingly enough, it actually escapes all apostrophes. It doesn't seem to matter if they're encapsulated as double-quotes as well. One more test we could try is to see how it behaves if we escape our own apostrophes. SQL allows this if you pre-pend a "\" quote. Let's test out the form further.

### Escaping Our Own Quote
![image](https://user-images.githubusercontent.com/66766340/147104527-808aa288-bdd9-4112-904f-0bcefcb0649b.png)

Nice, we got the error, meaning we can start to affect the query. However, given that it escapes quotes, it may be safe to assume that the end quote is put in automatically. We may be able to escape the first quote, but there is still a pesky one at the end that would effect our ability to fully escape the string. Luckily, SQL, like any other programming language can comment with "-- ". 

So we know how to escape the first quote, but one way to escape the end quote, effectively closing the string would be to simply comment it out. My modified input looks like:
```MySQL
\'or 1=1;-- 
```
*make sure you have the trailing space after the comment symbol

### Closing the End Quote, Modifying Query
![image](https://user-images.githubusercontent.com/66766340/147105054-cf058c3f-01f4-4935-a616-dd1eba114c23.png)

Perfect, we've got ourselves another table dump!
