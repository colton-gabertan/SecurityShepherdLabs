# Insecure Cryptographic Storage Challenge 1

**Instructions:**

The result key has been encrypted to ensure that nobody can finish the challenge without knowing the secret key to decrypt it. However, the result key has been encrypted with a famous, but easily broken, Roman cipher. The Plain text is in English.
```
Ymj wjxzqy pjd ktw ymnx qjxxts nx ymj ktqqtbnsl xywnsl; rdqtajqdmtwxjwzssnslymwtzlmymjknjqibmjwjfwjdtzltnslbnymdtzwgnlf
```

## Lab Walkthrough

This is now an example of encryption, rather than encoding. In order to crack it, we need to know which cipher is used as well as the *key* information we need to solve it. Luckily by the hint, we know it is a Caesar's Cipher. Essentially, all a Caesar's Cipher does is shift or *rotate* the letters a certain amount of letters away from the original in order to spit out the ciphertext. 

Here we are given the string to decrypt. The way that it works in terms of how to actually code a cipher such as this one, we need knowledge of the ascii table. This is the format that computers can use in order to identify letters of the alphabet. 

### ASCII Codes of the Alphabet
![image](https://user-images.githubusercontent.com/66766340/147606782-71ccd3df-56bf-4583-bc60-dc9052984d04.png)

If you wanted to implement a Caesar's Cipher, also known as ROT13, we'd simply be working with the ascii values of the table, so 65-90 (UpperCase) & 97-122 (lowercase). Say Alice wanted to send Bob a ROT13-encrypted message, both of them would need to know the amount of letters that they will shift for the message. Furthermore, say Alice would like the rotational value to be 13, every letter will get shifted 13 letters over, wrapping each time it reaches the end of its section. 

Therefore if Alice wanted to send the capital letter "A", it would shift to the capital letter "N". For Bob to decrypt it, he would take the ascii value of "N", which is 78, subtract 13 to get 65 and translate it back to plaintext, "A". This is known as symmetric encryption, as there is only one key used to both encrypt and decrypt data.

As you can see it is a pretty weak form of crypto as it would only take a max of 25 tries to crack the ciphertext. However, it serves as a gentle introduction to cryptography as we start to see other weak implementations.

Luckily CyberChef can also help us decrypt Caesar's Ciphers with its ROT13 tool. All we need to do is look for the rotation value that was used in the encryption of this message.

### Cracking Caesar's Cipher w/ CyberChef
![image](https://user-images.githubusercontent.com/66766340/147607634-3948b839-acc7-4d9f-851c-38456c0c2bfc.png)

In this case, it looks like it was shifted 21 times, and we've effectively broken this encryption.
