---
hidden: true
categories: 

    - cs
    - programming
    - dsa

description: My code for the exercises of the book Common sense DSA by Jay Wengrow. 
---

# Chapter 4: Speeding up your code with Big O

## Ex 4
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

## Ex 3
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

## Ex 4

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

# Chapter 8: Blazing fast lookups with hash tables

## Ex 1

{% highlight python %}

def find_intersection(array1, array2):
    larger_array = []
    smaller_array = []
    final_array = []
    dict1 = {}
    
    if(len(array1) >= len(array2)):
        larger_array = array1
        smaller_array = array2
    else:
        larger_array = array2
        smaller_array = array1

    # O(N)
    for elem in larger_array:
        dict1[elem] = True

    # O(M)
    for elem in smaller_array:
        if(dict1[elem]):
            final_array.append(elem)

    print("final_array = ", final_array)


def main():
    array1 = [1,2,3,4,5]
    array2 = [1,2,3]

    find_intersection(array1, array2)

if __name__ == "__main__":
    main()

{% endhighlight %}

## Ex 2

{% highlight python %}

def find_duplicate(array1):

    temp_dict = {}
    for elem in array1: 
        
        if elem not in temp_dict:
            temp_dict[elem] = True

        else:
            print(elem)
            break


    

def main():
    array1 = ["a", "b", "c", "d", "c", "e", "f"]

    find_duplicate(array1)

if __name__ == "__main__":
    main()

{% endhighlight %}

## Ex 3

{% highlight python %}

def find_missing_character_in_string(string):
    temp_dict = {}
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','o','p','q','r','s','t','u','v','w','x','y','z']

    # O(N)
    for char in string:
        if char not in temp_dict:
            temp_dict[char] = True

    # O(N)
    for letter in letters:
        if(letter not in temp_dict):
            print(letter)

def main():
    string = "the quick brown box jumps over a lazy dog"
    find_missing_character_in_string(string=string)

if __name__ == "__main__":
    main()

{% endhighlight %}

## Ex 4

{% highlight python %}

def find_first_non_duplicated_char(word):
    temp_dict = {}

    for char in word: 
        if char not in temp_dict:
            temp_dict[char] = 1
        else:
            temp_dict[char] += 1

    for char in word:
        if char in temp_dict:
            if(temp_dict[char] == 1):
                print(char)
                break
        

def main():
    word = "minimum"

    find_first_non_duplicated_char(word)

if __name__ == "__main__":
    main()

{% endhighlight %}

# Chapter 10: Recursively Recurse with Recursion

## Ex 4

{%highlight python%}

def print_just_numbers(array):
    for elem in array:
        if isinstance(elem, int):
            print(elem)

        elif isinstance(elem, list):
            print_just_numbers(elem)

array = [1, 2, 3, [4, 5, 6], 7, [8, [9, 10, 11, [12, 13, 14]]], [15, 16, 17, 18, 19, [20, 21, 22, [23, 24, 25, [26, 27, 29]], 30, 31], 32], 33]

print_just_numbers(array=array)

{%endhighlight%}

# Chapter 13: Recursive Algorithms for Speed

## Ex 1

Given an array of positive numbers, write a function that returns the greatest product of any three numbers. The approach of using three nested loops would clock in at O(N3), which is very slow. Use sorting to implement the function in a way that it computes at O(N log N) speed. (There are even faster implementations, but we’re focusing on using sorting as a technique to make code faster.)

{%highlight python%}


def find_largest_product_of_three_nums(arr):
    arr.sort()

    if len(arr) >= 3:
        print("Largest product of any three possible numbers is: ", arr[-1]*arr[-2]*arr[-3])

    else:
        print("Not possible to print largest product of any three numbers in the list because there do exist less than 3 entries in the entire list.")

find_largest_product_of_three_nums([4, 3, 2, 6, 5, 1])

{%endhighlight%}

# Chapter 17: It Doesn't Hurt to Trie

## Ex 3 and 4

{%highlight python%}

class TrieNode:
    def __init__(self): 
        self.children = {} 

class Trie:

    def __init__(self): 
        self.root = TrieNode()

    def search(self, word): 
        currentNode = self.root
        
        for char in word:
            # If the current node has child key with current character:
            if currentNode.children.get(char):
                # Follow the child node:
                currentNode = currentNode.children[char]
            else:
                # If the current character isn't found among
                # the current node's children, our search word 
                # must not be in the trie:
                return None
        return currentNode
    
    def insert(self, word): 
        currentNode = self.root
        for char in word:
            # If the current node has child key with current character:
            if currentNode.children.get(char):
                # Follow the child node:
                currentNode = currentNode.children[char]
            else:
                # If the current character isn't found among
                # the current node's children, we add 
                # the character as a new child node: 
                newNode = TrieNode() 
                currentNode.children[char] = newNode
                # Follow this new node: 
                currentNode = newNode
        # After inserting the entire word into the trie, 
        # we add a * key at the end: 
        currentNode.children["*"] = None

    def collectAllWords(self, node=None, word="", words=[]): 
        # This method accepts three arguments. The first is the
        # node whose descendants we're collecting words from.
        # The second argument, word, begins as an empty string,
        # and we add characters to it as we move through the trie.
        # The third argument, words, begins as an empty array,
        # and by the end of the function will contain all the words 
        # from the trie.

        # The current node is the node passed in as the first parameter, 
        # or the root node if none is provided:
        currentNode = node or self.root
        # We iterate through all the current node's children: 
        for key, childNode in currentNode.children.items():
            # If the current key is *, it means we hit the end of a 
            # complete word, so we can add it to our words array: 
            if key == "*":
                words.append(word)
            else: # If we're still in the middle of a word:
                # We recursively call this function on the child node. 
                self.collectAllWords(childNode, word + key, words)
        return words
    
    def autocomplete(self, prefix): 
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode)
    
    ###################### Addition by Kumar ###########################
    
    def print_all_keys(self, current_node=None):
        # Initialize to root only if this is the very first call
        if current_node is None:
            current_node = self.root

        for key, node in current_node.children.items():
            print(key)
            
            # Only recurse if the node exists (is not None).
            # This prevents us from following the "*" key, which points to None.
            if node: 
                self.print_all_keys(current_node=node)

    def autocorrect(self, user_str = None):
        if not user_str :
            return
        
        current_node = self.root
        word = ""
        is_autocorrect_used = False
        
        for user_char in user_str:
            
            if current_node.children.get(user_char): 
                # current_node.children has user_char key. Proceed as usual

                current_node = current_node.children[user_char]
                word += user_char
            
            else:
                #current_node.children does not have user_char key. Start autocorrect procedure

                is_autocorrect_used = True

                return word + self.collectAllWords(current_node)[0]

        if(is_autocorrect_used):
            return f"autocorrect applied for {user_str}: {word}"
        else:
            return f"autocorrect NOT applied for {user_str}"


trie = Trie()

trie.insert("cat")
trie.insert("catnap")
trie.insert("catnip")

print(trie.autocorrect("catnar"))
print(trie.autocorrect("ca"))
print(trie.autocorrect("caxasfdij"))

{%endhighlight python%}