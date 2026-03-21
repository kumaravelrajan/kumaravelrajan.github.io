---
categories:

    - programming
    - go

description: A blog explaining why understanding UTF-8 encoding is crucial to working with strings in Go. 

published: true

title: The curious case of len(Go strings)
---

# Why Go, why?

Consider the following example of dealing with strings in Go. 

```go

s := "京"

len(s)                 // 3

r := []rune(s)  

len(r)                // 1

```

To understand why this is the way this is, we need to dive a bit into Unicode and UTF-8 encoding. 

# ASCII vs Unicode vs UTF-8

A character encoding scheme is a standardized mapping of characters to numeric (binary) values, since data must ultimately be represented in binary at the hardware level. 

As you might be familiar, at the start of the computer revolution there existed only ASCII encoding. This encoding scheme used 7 bits and was enough to encode uppercase and lowercase English alphabets along with 32 control characters like newline, comma etc. 

However, as computers became widespread in the non-english speaking world as well, these languages also had to be supported in computers. 

This is why the Unicode standard was published in 1988. This standard took every single symbol in every single human language and assigned a unique codepoint to it. 

The thing with Unicode though is that it does not tell us how to implement these codepoints in binary. This is why various encoding schemes called UTF (Unicode Transformation Format) are present. 

- UTF-32

    This is possibly the simplest scheme to convert from Unicode codepoint to binary. A UTF-32 file can be seen as an array of characters with each index spanning 32 bits (4 bytes). A file is nothing but a array of 32 bit characters stacked one after the other. Each index consists of one Unicode codepoint. 

    But as can be imagined, this encoding scheme creates pretty large files. Even for plain English characters that under ASCII only occupied 1 byte each, UTF-32 scheme assigns each such character 4 bytes. 

- UTF-16

    This scheme figuratively and literally lies between UTF-32 and UTF-8 schemes. 

    The reason I say this is that, in this scheme every character occupies 16 bits. But the problem is that this break compatibility with ASCII. This means ASCII documents opened in UTF-16 software or vice-versa would break. 

    This scheme was widely adopted by Microsoft before UTF-8 became the dominant encoding scheme. 

- UTF-8

    This is the dominant encoding scheme across the web today. 

    ![UTF 8 is the most popular encoding scheme.](/assets/images/posts/go_utf8/Unicode_Web_growth.png)
    <br>
    However, unlike UTF-16 and UTF-32 this isn't a fixed width encoding scheme. Depending on the character being encoded, in UTF-8 it can occupy anywhere between 1-4 bytes. 

    The impressive thing about UTF-8 is that it is both forward and backwards compatible with ASCII. It's quite interesting to learn about how computer scientists managed this feat. If you'd like to know more about this, I can recommend you this youtube video which really is an excellent resource to understand UTF-8 encoding. 

    Spoiler alert: The famous Ken Thompson, who curiously also created Go, also plays a role in making UTF-8 a self-synchronising encoding scheme. 

    <iframe width="560" height="315" src="https://www.youtube.com/embed/vpSkBV5vydg?si=XinfxvpDwA0gEufI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>Here</iframe>

    <br>

    **The important fact to remember for our purposes is that UTF-8 characters can take anywhere between 1 and 4 bytes.** 

# The chinese character 京

The following facts are important to understand Go's behavior in the code sample shown at the start. 

1. Go strings are Unicode/UTF-8 compliant. 

    Strings are implemented as a read-only byte array. 
    
    In Go, bytes are simply an alias for uint8. 

    So in essence, Go strings are an array where each index spans 8 bits. Since utf-8 strings can span from 1-4 bytes this means from a byte array perspective, all these bytes are stacked one after the other. The Go language takes care of fetching the corresponding unicode character when we iterate through strings using the range function in loops. But this doesn't change the fact about the underlying data structure. 

2. rune in Go holds one Unicode codepoint

    Rune is a Go type that is an alias for int32. A rune array is hence an array where each index spans 4 bytes. This is perfect for unicode since any codepoint can only reach a maximum of 4 bytes. 

    In fact, **in the Go world a rune is what is used to denote a unicode character.** 

    When we convert a string (byte array) to a rune array, the unicode characters possibly spanning multiple bytes in the []byte are condensed into the original codepoint and stored in the []rune.

    Hence, []rune obtained from converting a []byte always stores 1 unicode character per index with each index in the []rune spanning 4 bytes.

3. Summary
  
    |Character|Unicode / UTF-32|UTF-8|
    |-|-|-|
    |京|**U+4EAC**|**0xE4 BA AC**|

    In UTF-8, 京 takes up 3 bytes. 

# Go strings are Unicode / UTF-8 compliant

Now the below behavior by Go should makes sense. 

```go

s := "京"                // string is read only []byte
                        //  byte = uint8 = 1 byte
                        // Representation: s = | 0xE4 | 0xBA | 0xAC |

len(s)                  // 3

r := []rune(s)          // rune = int32 = 4 bytes
                        // 1 UTF-8 char is max 4 bytes
                        // Representation: r = |0x00004EAC| (actual unicode codepoint)

len(r)                  // 1

```

# Why does this matter?

Imagine you are building a Twitter style character limit of 280 characters which is to be applied to each tweet. 

Simply considering the user input as a Go string and doing len(user_input) would be a bug filled implementation. Users typing in non-english languages or even english speakers using emojis (which utilize 4 bytes under UTF-8) would reach the character limit faster than users typing plain english. 

Hence, the user input needs to be considered as a []rune i.e. a rune slice and then we would get the unicode character count which is what we want. 

![Twitter style character counter](/assets/images/posts/go_utf8/Twitter_char_count.png)



