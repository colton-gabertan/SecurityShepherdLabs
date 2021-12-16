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

I'd like to switch up the way we reach our flag for this challenge to showcase a few more useful features of BurpSuite. Thanks to real-world breaches and security research, many hashing algorithms have been defeated and are considered outdated and bad practice to be using. It is mostly a matter of identifying which algorithm is being used, which you can only develop intuition for with experience and a bit of due diligence. 

So, let's fire up Burp and take a look at the packet we will be sending out!

### Burpsuite demo
<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/IDOR-Challenge-2/IDORchallenge2-1.gif">

As we can see, I had Pat McKenana selected, and the value we are sending corresponds with the has we can find in the HTML. Now onto use the built-in decoder that Burp offers. Copy the value and head over to the decoder tab in Burp. Play around with the different encoding algorithms until you see the decoded value. It will set us up nicely once we know what is being obscured.






[IDOR Challenge 1]: https://github.com/colton-gabertan/SecurityShepherdLabs/blob/IDOR-Challenge-1/README.md
[this article]: https://www.okta.com/identity-101/hashing-algorithms/
