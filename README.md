# Insecure Direct Object References Challenge 2

**Instructions:**

The result key for this challenge is stored in the private message for a user that is not listed below...

## Lab Walkthrough

This challenge is essentially the exact same as [IDOR Challenge 1]. We are presented with the web form, and some options to submit as our request to the server. As we are performing an IDOR, our goal is to reference data that should not be accessible to us. Following the same methodolgy as the last challenge, we find a familiar sight; however, the values look different.

### HTML of form
![image](https://user-images.githubusercontent.com/66766340/146283701-e22bcfb9-bf57-441c-9907-87f801084a5f.png)

If this is your first time seeing hashed data, it's a peek of what a lot of real-world web apps use to help obscure data. Obscuring data serves multiple purposes. One is to keep those values hidden, but readable to the server. Another is actually for authentication of data, which in turn can also uphold the integrity of our users. To understand how data is authenticated by these hashes, you must first understand how hashing works.

To obscure data, there is a method called *hashing*. Hashing is a one-way algorithm that spits out a digest of data that looks random and is technically mathematically uncrackable to humans. 

It serves as an authentication medium because these algorithms always spit out the **same** value for the **same** data. If even one bit is different, the hash will look completely different, indicating that the data is being tampered with. Hashing and encryption deserve a week in and of itself, but as a bit of a teaser, I encourage you to read [this article], which is from the company that our own university uses for web app security.

Thanks to the work of security research and real-world breaches, many of these hashes have been discovered; therefore, rendering many hashing algorithms obsolete and considered bad practice to be using. This has lead to the development of rainbow tables, which we will cover in later lessons. But for now, we can take advantage of a these rainbow tables [here]

Let's start cracking those hashes, recognizing a pattern!

### Crackstation demo
<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/IDOR-Challenge-2/IDORchallenge2-0.gif">

Crackstation also features the ability to identify the algorithm used to hash the value, in this case, md5.

After some hash cracking, a pattern emerges: 2, 3, 5, 7, 11...

They're prime numbers, so the next logical number in the list would be 13; however, we can't send 13 in plaintext, as this app is a bit more sophisticated, at least accepting hashes in the request. So we will need to find the md5 hash for the number 13. A quick google search for a tool to create md5 hashes and we can create the hash for our next value.

Using [this tool], I was able to come up with a hash for the value 13
```
c51ce410c124a10e0db5e4b97fc2af39
```

So, let's plug it in and send out our tampered request!



[IDOR Challenge 1]: https://github.com/colton-gabertan/SecurityShepherdLabs/blob/IDOR-Challenge-1/README.md
[this article]: https://www.okta.com/identity-101/hashing-algorithms/
[here]: https://crackstation.net/
[this tool]: https://www.md5hashgenerator.com/
