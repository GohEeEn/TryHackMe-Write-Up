# c4ptur3-th3-fl4g write-up
A beginner-level CTF challenge as one of the [TryHackMe room](https://tryhackme.com/room/c4ptur3th3fl4g), which focus in [Cryptography](https://ctf101.org/cryptography/overview/) and [Forensics](https://ctf101.org/forensics/overview/) that divided into 5 different tasks. 


## [Task 1] Translation & Shifting
Topic : Cryptography
* Translate, shift and decode the following questions. 
* Note : Answers are __all case sensitive__

Personally recommend to use [CyberChef](https://gchq.github.io/CyberChef/) as a tool to solve most of the questions here easier.

### #1 Leet/1337/L33T

[Leet](https://simple.wikipedia.org/wiki/Leet) is an alternative alphabet set that general for English language that used mostly on internet. It can also applies on those language that constructed similarly to english alphabet set, eg. German and Spanish

It can be confusing at first, while considering those 'weird' (non-alphabetic) characters and guess with their nearest lower/uppercase alphabet helps a lot in translation. 

#### Cipher : c4n y0u c4p7u23 7h3 f149?

#### How to solve : 
* Translate by using this [tool](http://www.robertecker.com/hp/research/leet-converter.php), or
* By guessing (pretty straight forward here) , ie.
  * 4 > A > a
  * 0 > O > o
  * 7 > T > t
  * 2 > |2 > R > r 
  * 1 > l
  * 9 > g

#### Solution : can you capture the flag?

### #2 Binary to ASCII characters

Binary is a number representing system using only 2 digits (0 & 1), and it is also digital representation of text and data in computing. 

[ASCII (American Standard Code for Information Interchange)](https://en.wikipedia.org/wiki/ASCII) code is one of the most common character encoding standard for electronic communication. It is prevalent on computers, telecommunications equipment and other devices. As a [unicode](https://en.wikipedia.org/wiki/Unicode), ASCII code can be represented in 8, 16 or 32-bit binaries, which means each ASCII character can be represented by a certain length of binraies.

#### Cipher : 	
01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001

#### How to solve : 
* This cipher is delimited by whitespace, and each binaries are 8-bit long, thus it is in [UTF-8](https://en.wikipedia.org/wiki/UTF-8) format.
* The easiest way is to use the recommended tool CyberChef to decrypt it.
* Basically each binary value correponds to specific ASCII character, according to the [ASCII Table](https://www.rapidtables.com/code/text/ascii-table.html) here.
* For example, 
  * 01101100 -> l
  * 01100101 -> e
  * 01110100 -> t

#### Solution : lets try some binary out!

### #3 Base32 Encoding
[Base32](https://en.wikipedia.org/wiki/Base32) is a notation for encoding arbitrary byte (__1 char = 5-bit__) data, that using a certain restricted set of symbols that can be conveniently used by humans and processed by computers. The symbol set made up of 32 different characters, and an algorithm for encoding arbitrary sequences of 8-bit bytes into the Base32 alphabets. The most commonly used symbol set is [RFC4648](https://en.wikipedia.org/wiki/Base32#RFC_4648_Base32_alphabet), that include :
* Uppercase letters __A~Z__ (26 characters)
* Digits __2~7__ (6 characters)
* And symbol "__=__" for padding purpose, that is _required to yield correct decoded data when the size of transported data isn't confirmed_.

#### Cipher : MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======

#### How to solve : 
* Since all characters in the given cipher satisfies the criteria above, thus we can assume it is a Base32 encoded text.
* By using Cyberchef, which the default character set for translating Base32 cipher is the one mentioned above, we can get the plain text right away.

#### Solution : base32 is super common in CTF's

### #4 Base64
Similar to Base32 that mentioned above, [Base64](https://en.wikipedia.org/wiki/Base64) is a group of binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representaton. It is used especially when binary data, such as images or video which is transmitted over systems in a plain-text (ASCII) format. The [scheme](https://en.wikipedia.org/wiki/Base64#Base64_table) contains 64 characters with size __1 char = 6-bit__, and the most common [MIME](https://en.wikipedia.org/wiki/MIME)'s 64 scheme contains :
* Uppercase letters : __A~Z__ (26 chars)
* Lowercase letters : __a~z__ (26 chars)
* Decimal Digits : __0-9__ (10 chars)
* 2 additional symbols '__+__' and '__-__'
* Padding symbol '__=__' (not included)

#### Cipher : RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg==

#### How to solve :
* Since all characters in the given cipher satisfies the criteria above, thus we can assume it is a Base64 encoded text.
* By using Cyberchef, which the default character set for translating Base64 cipher is the one mentioned above, we can get the plain text right away. 
  
#### Solution : Each Base64 digit represents exactly 6 bits of data.

### #5 Hexadecimal to ASCII characters
[Hexdecimal](https://en.wikipedia.org/wiki/Hexadecimal) is a number system that represents numbers using a base of 16. It consists the following characters :
* Digits    : __0 ~ 9__
* Letters   : __A ~ F (or a ~ f)__, that indicates the numerical values __10 ~ 15__

#### Cipher : 68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 

#### How to solve : 
* Since it consists letters __c, d and f__ within the decimal values, thus we can assume it is hexadecimal value.
* By using CyberChef, since the default delimiter of the translation operator is whitespace, hence the plain message can be found directly.

#### Solution : hexadecimal or base16?

### #6 ROT13 Encryption
[ROT13](https://en.wikipedia.org/wiki/ROT13) is a simple __letter [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher)__ that _replaces a letter with the 13th letter after it in the general alphabet set __(A~Z : id = 1 ~ 26)__._ 

Since there are 26 characters in the alphabet set, thus the encryption and the decryption algorithm are the same (ie. 13 * 2 = 26), that make it considered to a weak encryption. Example :

Plain     | Encrypted |How
 ---      | ---       | ---
A (id=1)  | N (id=14) | 1 + 13 = 14
N (id=14) | A (id=1)  | 14-13 = (14+13) __mod 26__ (wrap-up) = 1

#### Cipher : Ebgngr zr 13 cynprf!

#### How to solve : 
* Based on the given cipher, assume the numerical value is unchanged.  Also, take the integer value 13 as a hint since other characters are all letters, thus letter substitution encryption is in mind.
* Search any encryption method on Cyberchef that related to integer 13
* Apply ROT13 operator and the plain message is returned

#### Solution : Rotate me 13 places!

### #7 ROT47
[ROT47](https://rot47.net) is a derivate of ROT13, which is a simple character substitution cipher that replaces a character within the [ASCII range [33, 126]](https://www.asciitable.com) (ie. 7-bit printable characters). 

Just like ROT13, ROT47 is also an _invertible algorithm_, ie. same algorithm for encoding and decoding, while _plus 47 instead of 13_, since ASCII range for ROT47 = 33 ~ 126 -> __(126 - 33 + 1) / 2 = 94 / 2 = 47__

Example (id=ASCII value) :

Plain     | Encrypted |How
 ---      | ---       | ---
A (id=65) | p (id=112)| 65 + 47 = 112
p (id=112)| A (id=65) | 112 - 47 = (112 + 47) __mod 94__ (wrap-up) = 65
/ (id=47) | ^ (id=94) | 47 + 47 = 94

#### Cipher : *@F DA:? >6 C:89E C@F?5 323J C:89E C@F?5 Wcf E:>6DX

#### How to solve : 
* Since all characters have the ASCII value within the range above, so we can assume it is encrypted with ROT47
* Select the ROT47 operator and the plaintext is obtained.

#### Solution : You spin me right round baby right round (47 times)

### #8 Morse Code
[Morse code](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf) is an encryption method that used in telecommunication to encode letters (regardless lowercase or uppercase) and digits. It takes a standardized sequences of 2 different signal duration, __dots and dashes__ or __dits and dahs__ (ie. '**.**' and '**-**'). 

The characteristics of morse code are :
* Each morse code symbol is formed by a sequence of dots and dashes
* _**Dot duration** is the basic unit of time measurement in Morse code transmission_
* _**Dash duration** is three times of the dot duration_
* Each dot or dash within _a character_ is followed by *period of signal absence*, called a __space__, which _equals to per dot duration_.
* Spacing and length of the signals : (**signal=1, absence=0**)
  * *Dot duration=1* && *dash duration=111*
  * The _space between the signals forming the same letter_ is equal to **1 space (0)**
  * The _space between 2 letters_ is equal to **3 dot durations (000)** 
  * The _space between 2 words_ is equal to **7 dot durations (0000000)**
* Example String : "As I said"

Word  | Each letter | Total dot duration / Word
------| ------------------- | ----------------------
As    | <ul><li>a = **.-** = 10111</li><li>s = **...** = 10101</li></ul> |5 * 2 (a, s) + 3 * 1 + 7 = 20
I     | <ul><li>I = **..** = 101</li></ul>| 3 (I) + 3 * 0 + 7 * 1 = 10
said  | <ul><li>s = **...** = 10101</li><li>a = **.-** = 10111</li><li>i = **..** = 101</li><li>d = **-..** = 1110101</li></ul>| 5 * 2 (s, a) + 3 (i) + 7 (d) + 3 * 3 + 7 = 36 
TOTAL | | 20 + 10 + 36 = 66

Thus, it takes 66 dot durations to transmit the full message "As I said" in Morse code


#### Cipher : 
__- . .-.. . -.-. --- -- -- ..- -. .. -.-. .- - .. --- -.
. -. -.-. --- -.. .. -. --.__

#### How to solve :
* By identifying the cipher pattern, we can be assure it is morse code encoded.
* The morse code in text here takes whitespace as space between characters, and newline as space between words
* By using operation in CyberChef with default setting, we can get the decoded message directly

#### Solution : TELECOMMUNICATION ENCODING / telecommunication encoding

### #9 Decimal to ASCII
Decimal here means the base10 value which we see commonly throughout the world, that represents digits from **0 to 9**.

#### Cipher : 85 110 112 97 99 107 32 116 104 105 115 32 66 67 68

#### How to solve : 
* The conversion here is done by referencing each whitespace-delimited decimal value that corresponding to [ASCII table](http://www.asciitable.com). Example :
  Decimal | Character
  ---     | ---
  85      | U
  99      | c
  115     | s

* By using CyberChef, the plaintext is obtained easily by using the right operator.

#### Solution : Unpack this BCD

### #10 Multiple Encryptions

The cipher in this question is encoded using multiple encryption methods.

#### Exception : Since the cipher of this question is too long, refers to the [link](https://tryhackme.com/room/c4ptur3th3fl4g#1) here to view the cipher on [Task 1] #10

#### How to solve : 
* CyberChef is preferred since it has the ability to apply multiple operators in sequence and order them, to obtain the final result
* Also, it does basic analysis to any given inputs and suggest possible operator(s) to use based on that.
* By using CyberChef, we are able to disassemble the encryptions :
  1. **Base64**, since the given cipher consists of both upper and lowercase letters, and ended with an equal symbol "**=**"
  2. **Morse code**, since the decoded cipher contains only *dots and dashes*
  3. **Binary to ASCII**, as only _digits 0 and 1_ are found in the decoded cipher
  4. **ROT47**, since the decoded cipher contains *letters and certain symbols in ASCII range [33, 126]*
  5. **Decimal to ASCII**

#### Solution : Let's make this a bit trickier...

## [Task 2] [Hashes](https://ctf101.org/cryptography/what-are-hashing-functions/)
* A hash function is any function that can used to map data of arbitrary size onto data of a fixed size, and the returned value called __hashes (also hash values, hash codes or digests).__
* There are 3 ways suggested by the author of this room :
  * [CyberChef](https://gchq.github.io/CyberChef), to analyze the given hashes
  * [Hashcat](https://hashcat.net/wiki/doku.php?id=hashcat) bruteforce, to unhash (*Harder and Time-Consuming*)
  * [md5hashing.net](https://md5hashing.net/hash/), to find the corresponding plain message  (*Recommended*)
* Note : _What have been done in mdhashing.net is not decrypting the hash (impossible in short time, ie. Hashcat) but reverse lookup records in their gigantic database._

### #1. [MD2](https://en.wikipedia.org/wiki/MD2_(hash_function))

#### Hashes : 39d4a2ba07e44421c9bedd54dc4e1182
#### Hint   : This method of encyrption is no longer considered 'secure'. It's an MD, but which one?

#### How to solve :
* MD (Message-Digest algorithm) series : MD2, MD4, MD5 and MD6, that sorted ascendingly according to their date released.
* So far MD2 (the earliest) is only one that not longer considered as a secure one-way hash function from [2004](https://en.wikipedia.org/wiki/MD2_(hash_function)#Security). Thus, we can be sure that the hint is referring to MD2 Hashing Algorithm.
* By using md5hashing.net with Hash type MD2, the following decoded message got returned.

#### Solution : MDwhat?

### #2. [MD4](https://en.wikipedia.org/wiki/MD4)

#### Hashes : e0418e7c6c2f630c71b2acabbcf8a2fb
#### Hint   : Better than MD2, but not as good as MD5

#### How to solve :
* Since we know MD4 is found after MD2 and before MD5 among the entire MD series, we can assume it is talking about _MD4 hashing algorithm_.
* By using md5hashing.net with Hash type MD4, the following decoded message got returned.

#### Solution : digest the message algorithm

### #3. MD5
An MD5 hash is created by taking a _string in any length and encoding it into a 128-bit fingerprint_. Encoding the same string using it will always result in the same 128-bit hash output. 

#### Hashes : efbd448a935421a54dda43da43a701e1

#### How to solve : 
* By using the hash analysis feature of CyberChef, there is a list of hash functions that assumed to encode the message, according to the hash, byte and bit length of the hashes.
* As MD5 is on top of the list, so here we assume it is encoded by using MD5 hash function
* By using md5hashing.net with Hash type MD5, the message has been decrypted and the output as follow.

#### Solution : 128-bit of delicious hash values

### #4. [NTLM Algorithm](https://openwall.info/wiki/john/NTLM)
It is a hashing algorithm used in Microsoft network security protocols, which specifically called [NTLM Authentication Protocol](http://davenport.sourceforge.net/ntlm.html). This hashing algorithm is actually based on [MD4 Algorithm](https://openwall.info/wiki/john/MD4), to store encoded passwords as an __128-bit__ value in Windows.

#### Hashes : 11FE61CE0639AC2A1E815D62D7DEEC53

#### Hint   : SoftMicro

#### How to solve :
* Note : I have spend actually quite a while to solve this question, since the encryption method here is not that common.
* I have tried all the encryption methods from the analysis of CyberChef and decode with them on md5hashing.net. However, none of them works.
* Back to the given hint and after some research done, I found out Microsoft does have a hashing algorithm that based on MD4, which is NTLM Algorithm.

#### Solution : Microsoft has encryption?

### #5. [SHA512](https://www.movable-type.co.uk/scripts/sha512.html)
SHA512 is part of the [SHA-2](https://en.wikipedia.org/wiki/SHA-2) cyptographic hash function set that designed by United State NSA. It is named SHA512 since it _generates an almost-unique 512-bit (64 bytes) signature for an arbitrary text, by operating on a 1024-bit message blocks, based on 64-bit words_.

#### Hashes : a361f05487b879f25cc4d7d7fae3c7442e7849ed15c94010b389faafaf8763f0dd022e52364027283d55dcb10974b09e7937f901584c092da65a14d1aa8dc4d8

#### Hint   : My heart goes SHAlalalala SHA lala 512 times!

#### How to solve :
* Based on the hint, we can suggest that it is talking about SHA512
* It can be confirmed by analyse the given hash with CyberChef.
* By using md5hashing.net, we can obtain the encoded message directly.

#### Solution : 1024 bit blocks!

### #6. SHA256
SHA256 is also part of the [SHA-2](https://en.wikipedia.org/wiki/SHA-2) cyptographic hash function set, while they are different in :

Property              | SHA-256   | SHA-512
---                   | ---       | ---
Max Input size        | 2^64 bits | 2^128 bits
Size/Block            | 512-bit   | 1024-bit
Output size           | 256-bit   | 512-bit

#### Hashes : d48a2f790f7294a4ecbac10b99a1a4271cdc67fff7246a314297f2bca2aaa71f

#### How to solve :
* Based on hash analysis, it assumes that this hash is encoded with SHA-256 in the highest possibility.
* The result can be obtained directly from md5hashing.net

#### Solution : Commonly used in Blockchain

### #7. SHA1
[SHA-1 (Secure Hash Algorithm 1)](https://en.wikipedia.org/wiki/SHA-1#SHA-0) is a cryptographic hash function which takes an input with max size 2^64 bits, and produces a 160-bit (20 bytes) hash value as output. A SHA-1 hash value is typically expressed in hexadecimal, 40 digits long.

#### Hashes : a34e50c78f67d3ec5d0479cde1406c6f82ff6cd0

#### Hint   : The First SHA

#### How to solve :
* We can expect it is SHA-1 hash function based on the given hint (ie. SHA family : SHA-1, SHA-2 & SHA-3, since SHA-0 is similar to SHA-1, thus not included)
* It can be confirmed by the hash analysis of CyberChef.
* The original message can be obtained by using md5hashing.net

#### Solution : The OG

## [Task 3] [Spectrograms](https://en.wikipedia.org/wiki/Spectrogram)
Topic : Forensics
* A **spectrogram** is a _visual representation of the spectrum of frequencies of a signal as it varies with time_. 
* When applied to an **audio signal**, spectrograms are sometimes called _sonographs, voiceprints, or voicegrams_. 
* When the data is represented in a *3D plot* they may be called __waterfalls__.

#### Given : [secretaudio.wav](./secretaudio.wav)
#### Hint : Audacity
#### How to solve :
* The '[Audacity](https://www.audacityteam.org)' from the given hint is actually an open source audio software, enable us to analyse an audio. However, since I dislike to download a whole software for just a question, thus I found sufficient tool online.
* By using [online spectrum analyzer](https://academo.org/demos/spectrum-analyzer/), it gave us a graph of all frequencies that are present in an audio at a given time, while playing it.
* By playing this audio that last 2 seconds, we can find the spectrogram actually form a secret message.

#### Solution : Super Secret Message


## [Task 4] [Steganography](https://en.wikipedia.org/wiki/Steganography)
Topic : Forensics
* Stegonagraphy describes the __action to conceal a message/file within an appropriate carrier__, that can be a message, image, video or an audio.

#### Given :
![A cute dinosaur is sitting on a bowl of spaghetti](./stegosteg.jpg)

#### How to find :
* By using this [steganographic decoder](https://futureboy.us/stegano/decinput.html), it extracts the plaintext within the given image.

#### Solution : SpaghettiSteg

## [Task 5] [Security through obscurity](https://en.wikipedia.org/wiki/Security_through_obscurity)
Topic : Forensics
* Security through obscurity is the reliance in security engineering on the secrecy of the design or implementation as the main method of providing security for a system or component of a system.

#### Given : 
![Meme image](./meme.jpg)

#### Questions 
Both answers can be found by **extract string components** from the given image file. It can be done by either CyberChef Strings operator, or open the file with text editor (eg. notepad++ or vscode), which match the given hint : __get "inside" the file -> metadata__

1. Download and get 'inside' the file. What is the first filename & extension?
   * Hint     : Obscure Steg
   * Solution : hackerchat.png

2. Get inside the archive and inspect the file carefully. Find the hidden text.
   * Hint     : Answer is case sensitive
   * Solution : AHH_YOU_FOUND_ME! 


### References :
* [Morse code : How to communicate with morse code](https://www.wildernessarena.com/environment/signaling/how-to-communicate-with-morse-code-using-visual-audio-pressure-communication)
* [Hashcat Basic Tutorial](https://resources.infosecinstitute.com/hashcat-tutorial-beginners/)
* [Descriptions of SHA-256, SHA-384 and SHA-512](http://iwar.org.uk/comsec/resources/cipher/sha256-384-512.pdf)
* [Difference of SHA-256 & SHA-512](https://crypto.stackexchange.com/questions/55658/difference-between-sha-512-sha-512-half-sha-256)