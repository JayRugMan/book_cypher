# book_cypher
A place where files are books and strings aspire to be digits


## What Is This, Even

### 1st, What is a Book Cypher
I book cypher is a string of numbers that reference a page, line, and word in a 
specific book (or with the bible, page, verse, word), then taking a list of 
these string, you can devise and send messages to someone who posesses the same 
book. Only if the book is know can the list of digits be de-cyphered. For 
example, using the Church of Jesus Christ of Latter-day Saints edition of King 
James version of the Holy Bible. 

```
149 5 16; 837 21 19; 1183 2 5; 1329 17 9
```

The key is the book; the book is the key. Basically, if you don't know what 
book is used, you can _in no way_ decipher the message. Even if you had a 
Bible, but it's a different version or edition, you still won't get the right 
message.


### How Can This Be Done Digitally?
Well, any file can be a book - even corrupt files. Using base64, any string of 
1's and 0's can be turned into characters in the English alphabet. All you need 
is a line and line-position reference. And, since you're using a computer, 
which is much faster as processing, you can reference each character instead of 
each word. By using python, you can process these data structures quickly and 
accross platforms.

Here is a file in base64:
```bash
 book_cypher (main ±)$ base64 book.py 
IyEvdXNyL2Jpbi9weXRob24zCicnJ1RoaXMgc2NyaXB0IGRvZXMgc3R1ZmYnJycKCmltcG9ydCBi
YXNlNjQKaW1wb3J0IHN5cwppbXBvcnQgYXJncGFyc2UKaW1wb3J0IHNlY3JldHMKZnJvbSBvcy5w
YXRoIGltcG9ydCBleGlzdHMKCgpkZWYgZ2V0X2FyZ3MoYXJndj1Ob25lKToKICAgICcnJ1VzZXMg
YXJncGFyc2UgdG8gZ2V0IGlucHV0JycnCgogICAgdGhlX2Rlc2NyaXB0aW9uPSdVc2luZyBhIGZp
bGUgYXMgYSAiYm9vaywiIGEgbWVzc2FnZSBjYW4gJyBcCiAgICAgICAgJ2JlIHByb2Nlc3NlZCBp
bnRvIGEgY29kZSBvciB2aXNlLXZlcnNhLicKICAgIGhlbHBfaGVscCA9ICcnJ1wKICAgICAgICAg
ICAgICAgICBZb3UgZ2V0IHRoaXMgaGVscGZ1bCBtZXNzYWdlIGJlZm9yZSBleGl0aW5nCgonJycK
ICAgIGJvb2tfaGVscCA9ICcnJ1wKICAgICAgICAgICAgICAgICBUaGlzIGRlc2lnbmF0ZXMgdGhl
IGZpbGUgdGhhdCBhY3RzIGFzIHRoZSAiYm9vayIgaW4gdGhlIGJvb2sKICAgICAgICAgICAgICAg
ICBjb2RlIGJ5IHVzaW5nIGl0cyBiYXNlNjQgZW5jb2RpbmcuIEl0IGNhbiBiZSBhbnkgdHlwZSBv
ZgogICAgICAgICAgICAgICAgIGZpbGUgLSAuaHRtbCwgLmltZywgLmpwZywgLm1wNCwgZXRjLiBL
ZWVwIGluIG1pbmQgaWYgdGhlCiAgICAgICAgICAgICAgICAgZmlsZSBpcyB0b28gc21hbGwsIHRo
ZSBlbnRyb3B5IHdpbGwgYmUgc21hbGw7IGlmIHRoZSBmaWxlIGlzCiAgICAgICAgICAgICAgICAg
dG9vIGJpZywgdGhlIHByb2Nlc3MgdGltZSBhbmQgcGVyZm9ybWFuY2UgbWF5IGJlIGltcGFjdGVk
LgoKJycnCiAgICBtZXNzYWdlX2hlbHA9JycnXAogICAgICAgICAgICAgICAgIFRoaXMgaXMgdGhl
IG1lc3NhZ2Ugc3RyaW5nIHRvIGJlIGVuY29kZWQuIEl0IGNhbiBiZSBhIHN0cmluZwogICAgICAg
ICAgICAgICAgIG9yIGEgcGxhaW4tdGV4dCBmaWxlLiBUaGlzIGNhbm5vdCBiZSB1c2VkIHdpdGgg
LWMvLS1jb2RlLgoKJycnCiAgICBjb2RlX2hlbHA9JycnXAogICAgICAgICAgICAgICAgIFRoZSBj
b2RlIGdvZXMgaGVyZS4gVGhpcyBjYW4gYWxzbyBiZSBhIGZpbGUgY29udGFpbmluZyB0aGUKICAg
ICAgICAgICAgICAgICBjb2RlIGluIHBsYWluIHRleHQuIFRoaXMgY2Fubm90IGJlIHVzZWQgd2l0
aCAtbS8tLW1lc3NhZ2UuCgonJycKICAgIHRoZV9lcGlsb2c9JycnXAoKbm90ZXM6CiAgT25seSB0
...
```

So this is the basic concept. If I generate "Hello World!" using a specific 
file as by "book", the resulting code can only be decoded using that exact 
file:

```bash
$ python3 book.py -b book.py -m 'Hello, world!'
22 18 78 5 109 7 41 44 52 31 2 7 84 46 94 29 68 11 148 21 94 18 24 15 69 7 62 36 108 40 117 61 58 31 24 6 12 11
$ python3 book.py -b book.py -c "22 18 78 5 109 7 41 44 52 31 2 7 84 46 94 29 68 11 148 21 94 18 24 15 69 7 62 36 108 40 117 61 58 31 24 6 12 11"
Message:
Hello, world!
```

You may be wondering how I was able to get the ',', SPACE, and '!' out of 
base64... simple, but it does add overhead. The python script turns a ',', for 
example, into a three-character string 'QXc', which is a sequense that isn't 
used in a normal English word. In our code above, this becomes '2 7 84 46 94 29':

```bash
$ python3 book.py -b book.py -c "2 7 84 46 94 29"                                                                                    
Message:
,
```

Then, as demonstrated above, this string is turned into 'QXc,' then back to ','