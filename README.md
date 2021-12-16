# Insecure Direct Object References Challenge 2

**Instructions:**

The result key for this challenge is stored in the private message for a user that is not listed below...

## Lab Walkthrough

This challenge is essentially the exact same as [IDOR Challenge 1]. We are presented with the web form, and some options to submit as our request to the server. As we are performing an IDOR, our goal is to reference data that should not be accessible to us. Following the same methodolgy as the last challenge, we find a familiar sight; however, the values look different.

### HTML of form
![image](https://user-images.githubusercontent.com/66766340/146283701-e22bcfb9-bf57-441c-9907-87f801084a5f.png)

Just to switch it up a bit, I'd like to showcase a few more features of BurpSuite, taking advantage of its ability to capture and modify packets, but also *decode* data as well. If this is your first time seeing encoded data, it's a peek of what a lot of real-world web apps use to help obscure data. Obscuring data serves multiple purposes. One is to keep those values hidden, but readable to the server. Another is actually for authentication of data, which in turn can also uphold the integrity of our users. To understand how data is authenticated by these hashes, you must first understand how hashing works.

To encode data, there is a method called *hashing*. Hashing is a one-way algorithm that spits out a digest of data that looks random and uncrackable to humans. It serves as an authentication medium because these algorithms always spit out the **same** value for the **same** data. If even one bit is different, the hash will look completely different, indicating that the data is being tampered with. This topic deserves a week in and of itself, but as a bit of a teaser, I encourage you to read [this article], which is from the company that our own university uses for web app security.



[IDOR Challenge 1]: https://github.com/colton-gabertan/SecurityShepherdLabs/blob/IDOR-Challenge-1/README.md
[this article]: https://www.okta.com/identity-101/hashing-algorithms/
