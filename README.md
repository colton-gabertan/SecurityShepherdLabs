# Insecure Cryptographic Storage

**Instructions:**

The decision has been made that the result key to this lesson should not be publicly available. To achieve this, the development team have decided to encode the result key with base64... recover it to complete the lesson.
```
YmFzZTY0aXNOb3RFbmNyeXB0aW9uQmFzZTY0aXNFbmNvZGluZ0Jhc2U2NEhpZGVzTm90aGluZ0Zyb21Zb3U=
```

## Lab Walkthrough

As we are familiar with *encoding* in base64, I'd like to mention that *encryption* and *encoding* are different and should not be used as interchangeable terms. We encode data so that it makes it more universally transferrable and readable by other parts of the web application. In some cases, encoding even helps to compress data a bit, increasing the transfer speed and reducing the virtual size of our data. 

Encryption, on the other hand, is intentionally used to hide data from malicious users. Encoding is made to be easily reversable into readable formats, while encryption always requires some other component in order to decrypt the ciphers. Therefore, using encoding as a means to encrypt is a very bad idea, instead, developers should be aware of best practices when it comes to handling sensitive information. There are well established cryptographic functions that are a reliable means to implement encryption into their applications.

Anyways, for this first lab, I'd like to introduce you to one of my favorite tools, [Cyber Chef]. It is extremely useful for situations in which you need to decode/encode data. It also supports some unique features regarding cryptographic topics, such as using specific algorithms to encrypt and decrypt data.

### Decoding Using CyberChef


[Cyber Chef]: https://gchq.github.io/CyberChef/
