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

    Haystack: "aaaaaa" (length N = 6).

    Needle: "aab" (length M = 3)

    - Here, for each character in the haystack:

        - The first character matches the first character of the needle ('a').

        - The inner loop checks subsequent characters to match 'a' and then fails at the last character 'b'.

        - This forces the inner loop to run nearly M times at every starting position.

    In this worst-case scenario, the naive substring search performs N × M character comparisons, illustrating the O(N x M) comparisons.

## Exercise 4

{%highlight ruby%}
def largest_product(array)
  largest_product_so_far = array[0] * array[1] * array[2]
  i = 0

  while i < array.length
    j = i + 1
    while j < array.length
      k = j + 1
      while k < array.length
        if array[i] * array[j] * array[k] > largest_product_so_far
          largest_product_so_far = array[i] * array[j] * array[k]
        end
        k += 1
      end
      j += 1
    end
    i += 1
  end

  return largest_product_so_far
end

{%endhighlight%}

Here, time complexity is $$O(N^3)$$. This is because the program has 3 nested loops that each runs approximately n times. Hence, this gives us $$O(N^3)$$ time complexity. 

Another way to look at this is that all unique combinations of three indices are chosen by the loops. This would be the same as 

\\[\binom{n}{3} = \frac{n!}{(n-3)!\,3!} = \frac{n(n-1)(n-2)\,\cancel{(n-3)!}}{\cancel{(n-3)!}\,3!} \approx n^3\\]