# Insecure Direct Object References Bank Challenge

**Instructions:**

To complete this challenge you must sign in to a bank account that has more than 5000000 euro in it. If you have more than this amount in your account, just sign out and back in again of the bank account to get the key, or open this level again.

## Lab Walkthrough

*Before getting started, as a general rule for the labs, we won't need to brute force with a list of values that contain over 100 items in it*

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

### Sending to Intruder and Editing Postions
<img src="https://github.com/colton-gabertan/SecurityShepherdLabs/blob/IDOR-Bank-Challenge/IDORbank0.gif">

Now that we have our payload positions set, time to navigate to the Payloads tab and specify the values we are going to feed to that position. In this case, we need to iterate through account numbers. Since we've made the newest account and our account number is 5502, it's a sound decision to decrement from 5502 - 5402. The settings to accomplish this will be listed below:

### Payload Settings
![image](https://user-images.githubusercontent.com/66766340/146334125-18c17705-ad22-4035-8ce0-4dfb1acac903.png)

In the upper right hand corner, there is a *start attack* button. Hit it and let Burp do its thing!

With these results, finding what we are looking for should be relatively easy. We can view the packet sent out and the response to our request. The length of the response is also listed. Given that we are looking for an account with a high balance, it is safe to say that the length will be longer than that of ours. Luckily we can sort by length by simply clicking on the label.

### Sniper Attack Results
![image](https://user-images.githubusercontent.com/66766340/146335583-8b36d9cd-46d4-4a9f-8156-8067b83f807d.png)
![image](https://user-images.githubusercontent.com/66766340/146335477-4381875a-7582-4ecd-b6ec-35e55d28c33f.png)

Looks like this millionaire is going to have a very bad day. We know that their balance is greater than $5000000, so we're going to transfer it to ourselves. Make sure to take note of their accountNumber: 5451.

With this information in mind, it's time to exploit it. We need to now intercept the packet that is responsible for requesting a transfer of funds.

### Transfer Funds Request
![image](https://user-images.githubusercontent.com/66766340/146336548-adc1f40f-a074-4882-bdc1-ec54049c8e9d.png)

Perfect! there is a field, for the senderAccountNumber & recieverAccountNumber & transferAmount. Let's tamper with this packet by inputting the values we found via the sniper attack.

### Tampered Packet
![image](https://user-images.githubusercontent.com/66766340/146336762-7b322e8b-caad-47b4-bc47-922a8cdbe50e.png)

Let's forward that packet, refresh our balance, and achieve an early retirement. We have successfully performed an IDOR manipulation to digitally rob a bank.
