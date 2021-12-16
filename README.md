# Insecure Direct Object References Challenge 2

**Instructions:**

To complete this challenge you must sign in to a bank account that has more than 5000000 euro in it. If you have more than this amount in your account, just sign out and back in again of the bank account to get the key, or open this level again.

## Lab Walkthrough

*Before getting started, as a general rule for the labs, we won't need to brute force a list of values that contain over 100 items in it*

Reading the prompt, it says we must sign in; however, IDOR isn't really a method that cracks passwords or user credentials. Instead what we can interpret is that we can reference an object that we shouldn't be able to. In this case, we should be able to reference another account's balance and transfer it to our own account.

To start off, simply create your own account and **don't forget your credentials** (the lab has no way of recovering them). Then sign in and we're going to walk through the application a bit. A good place to start would be viewing its source code via inspect.

### Inspecting how the bank works
![image](https://user-images.githubusercontent.com/66766340/146329661-3d123bad-3258-479f-8ac4-ff6024233633.png)

So with this information we can infer a couple of things. We are assigned an account number, mine is 5502. Given how primitive the web app is, I'd also infer that if we can somehow sift through the different accounts via the account number, we can find the information we are looking for and exploit it.

With this challenge I'd like to showcase a few more features that BurpSuite has to offer, so let's fire it up and get to hacking! However, first-things-first, how are we going to check the balance of the account id's we access? Notice that there is a *Refresh Balance* button. The packet that it sends out will be our entry point in accessing these accounts. With that in mind, let's capture that packet. We'll use it to iterate through 100 accounts, checking if we can catch a high roller. 

To do so, via your proxy, hit the Refresh Balance button and find it in the HTTP history. Features of this nature are usually a POST request.

### Refresh packet
![image](https://user-images.githubusercontent.com/66766340/146331307-b8f49109-7ad3-4a81-89d2-604b159684d5.png)

Nice, there's a field where we can take advantage of the accountNumber.

BurpSuite has a tab called Intruder which does what it sounds like it does. Here we are able to run all kinds of brute force attacks, but the one we'll focus on for now is called Sniper. Right-click on the packet and select *send to intruder*. Navigate to the tab and first to the Positions options.

Clear out the pre-set positions, highlight only the one we want to be changing and hit the Add button. Our payload is prepped for this attack now.


