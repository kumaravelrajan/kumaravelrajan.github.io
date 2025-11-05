---
hidden: true
categories: 

    - cs
    - programming
    - dsa

description: My code for the exercises of the book Common sense DSA by Jay Wengrow. 
---

# Chapter 4: Speeding up your code with Big O

## Exercise 4
{%highlight python%}
def greatestNumber(array):
    
    steps = 0
    currentGreatestNumber = array[0]

    for i in array:
        # Assume for now that i is the greatest:

        steps += 1
        if(currentGreatestNumber < i):
            currentGreatestNumber = i

    print("steps = ", steps)
    return currentGreatestNumber
        
        
greatestNumber([1,2,3,4,5])
{%endhighlight%}

# Chapter 7: Big O in Everyday Code

## Exercise 3
{%highlight ruby%}
def find_needle(needle, haystack)
    needle_index = 0
    haystack_index = 0

    while haystack_index < haystack.length
        if needle[needle_index] == haystack[haystack_index]
        # If the first characters of needle and haystack match proceed further. 

            found_needle = true

            while needle_index < needle.length
                if needle[needle_index] != haystack[haystack_index + needle_index]
                    found_needle = false
                    break
                end
                needle_index += 1
            end

            return true if found_needle
            needle_index = 0
        end

        haystack_index += 1
    end

    return false
end

{%endhighlight%}

Here, let haystack be of size N and needle be of size M. Outer loop iterates through each character in haystack of size n. For each  character in haystack that matches the first character of the needle, the inner loop checks the subsequent characters for a match. In the worst case, each character in haystack triggers M additional steps. Hence, Big-O is O(N*M).

1. Example: 

    The haystack consists of repeated characters, for example: "aaaaaa" (length N=6).

    The needle is almost the same repeated character sequence but differs at the last character, for example: "aab" (length M = 3)

    Here, for each character in the haystack:

    The first character matches the first character of the needle ('a').

    The inner loop checks subsequent characters to match 'a' and then fails at the last character 'b'.

    This forces the inner loop to run nearly M times at every starting position.

    In this worst-case scenario, the naive substring search performs N × M character comparisons, illustrating the O(NxM) comparisons.