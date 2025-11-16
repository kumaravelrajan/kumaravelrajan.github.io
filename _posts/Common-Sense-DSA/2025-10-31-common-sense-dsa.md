---
categories: 
    - cs
    - programming
    - dsa

description: My notes from reading A common sense guide to DSA - Jay Wengrow
title: Notes on "Common Sense DSA" by Jay Wengrow
---

# Chapter 1 : Why data structures matter

1. Data structure operations

    1. Read
    1. Search
    1. Insert
    1. Delete

1. Array

    1. They are allocated contiguous blocks of memory. 
    1. Read - 1 step
    1. Search - n step (where n is the size of the array)
    1. Insert 
        1. at end - 1 step
        1. at beginning - n + 1 steps
    1. Delete - n steps

1. Sets

    1. (simplification:) Same as arrays except that it does not allow duplicate entries. 
    1. Read, Search and Delete all same as normal arrays. 
    1. Insert operation has diff. time complexity. 

        1. Insertion at end: $$n + 1$$ steps. n steps for searching if the value we want to insert already exists and 1 step for actual insertion. 
        1. Insertion at beginning: $$n + n + 1 = 2n + 1$$ steps. n steps to search if value to be inserted already exists. n steps to shift every pre-existing value to the right. 1 step for the actual insertion at the beginning. 

# Chapter 2: Why algorithms matter

1. Even though we might settle on a data structure, even then the algorithm we choose to use on this data structure makes a massive difference in efficiency. *This* is why algorithms matter. 

1. Next data structure - Ordered arrays

    1. What is it? 

        It is a classic array except that all elements are at all times ordered in ascending order. 

    1. Insertion

        Insertion is more tedious that it was for classic arrays. When we want to insert a value, we first need to determine the index where it must be inserted, then move all elements starting from this index till the array end one step to the right and finally end up inserting the element in the given index. 

        Hence, insertion takes $$N + 2$$ steps irrespective of index to insert value in. When index is closer to beginning there are fewer comparisons and more shifts. When index is farther away from beginning there are more comparisons and fewer shifts. 

        Exception to this rule is that the index to insert is the end of the array. In that case we have N comparisons and 1 step for actual insertion. This makes it $$N + 1$$ step.

    1. Searching & binary search

        Having an ordered array enables us to use binary search which is orders of magnitude faster than our traditional linear search. Binary search only works with ordered arrays. 

        <mark>This is an exapmle of how choosing the right data structure (ordered arrays) enables us to choose an algorithm (binary search) that is much more efficient than any sorting algorithm available to us in a classic array.</mark>

        For binary search, though, each time we double the size of the array, we only need to add one more step. 



# Chapter 3: O Yes! Big O Notation

1. The key question: If there are N data elements, how many steps will the algorithm take?

1. O(N) and O(1)

    When an algorithm is O(N) it means when there are N data elements, the algorithm takes N steps. 

    1. Algorithm having O(N) complexity is known to have linear time complexity. 

        eg: linear search

    1. Algorithm having O(1) complexity means that it has constant time. i.e. Irrespective of the number of data elements (N) the algorithm always takes only 1 step. 

        eg: Reading from an array. 

1. The soul of Big O

    How will an algorithm's performance *change as the data increases?*

    In other words, it does not just want to tell us how many steps an algorithm takes for N data inputs. It wants to tell us how the number of steps increase as data changes. 

    This is why if we have an algorithm that takes 3 steps irrespective of the data size we do not write its complexity as O(3). Instead, we write it as O(1). As mentioned above, Big-O is concerned with the how the number of steps increase as data changes. In this regard, O(3) is the same as O(1).

1. Big-O and its pessimism

    Big-O can theoretically depict both best-case and worst-case scenarios. For example, in linear search we have the scenario where the searched element is present in index 0 itself. In this best case, linear search becomes O(1). But in the worst case it is as we know O(N).

    But generally, Big-O represents worst-case since this pessimistic approach can help in understanding how inefficient an algorithm can get in the worst-case scenarios and making choices accordingly. 

1. O (log N)

    Refers to algorithms that increase one step every time the data is doubled. In Big-O notation whenever we say O(log N) it is actually $$ O(log_2 N) $$. We just omit the base 2 for convenience. 

    Binary search has O(log N).

1. Sorting algorithm times from most to least efficient

    |Algorithm times arranged<br>from Most efficient to least efficient|
    |-|
    |O(1)|
    | O(log N) |
    | O(N) |

# Chapter 4: Speeding up your code with Big O

1. Bubble sort

    In each pass through, the highest unsorted value "bubbles" up to its correct position. 

    Bubble sort has $$ O(N^2) $$ complexity. This means bubble sort has *quadratic time*.

    Explanation of how bubble sort works is given in [wikipedia](https://en.wikipedia.org/wiki/Bubble_sort#Performance).

1. $$O(N^2)$$ complexity

    Very often (but not always), when an algorithm nests one loop inside another, the algorithm is $$O(N^2)$$.

    ```javascript

    function hasDuplicateValue(array) { 

        let steps = 0; // count of steps
        
        for(let i = 0; i < array.length; i++) { 
            
            for(let j = 0; j < array.length; j++) {
                
                steps++; // increment number of steps 

                // !!!
                if(i !== j && array[i] === array[j]) { 
                    return true;
                }
            }
        }
        console.log(steps); // print number of steps if no duplicates 
        return false;
    }

    ```

    Here, assume we have an array of length N. The outer loop iterates through every element of the array one by one. For every iteration of the outer loop, the inner loop iterates N times. So the statement in the inner loop (the comparison) is executes $$N^2$$ times in the worst case. Hence, this code has $$O(N^2)$$.

    The criteria here is, how many times is the code in the inner loop (the comparison statements) is executed in the worst case. 

    The above code can be optimized to an algorithm that has $$O(N)$$ instead of $$O(N^2)$$.

    ```javascript

    function hasDuplicateValue(array) {
        let steps = 0;
        let existingNumbers = [];

        for(let i = 0; i < array.length; i++) {
            steps++;
            
            if(existingNumbers[array[i]] === 1) {
                return true; 
            
            } else {
                existingNumbers[array[i]] = 1;
            }
        }

        console.log(steps); 
        return false;
    }

    ```

    Here, we get rid of the inner loop and keep just the outer loop. This means the new code has O(N).

1. Exercises

    - [Ex4]({% post_url Common-Sense-DSA/2025-11-02-code-examples-common-sense-dsa %}#exercise-4)

# Chapter 5: Optimizing Code with and Without Big O

1. Selection sort

    In each pass-through the lowest element is placed in the current starting position. It takes about half the number of steps bubble sort does. This means <ins> selection sort is twice as fast as bubble sort </ins>. If bubble sort had $$O(N^2)$$ then selection sort should have $$O(N^2/2)$$.

    But Big-O notation ignores constants. Therefore, in the Big O notation, Bubble sort and Selection sort both have $$O(N^2)$$ runtimes. 

    Animation of how selection sort works as given in [geeksforgeeks](https://www.geeksforgeeks.org/dsa/selection-sort-algorithm-2/).

1. Why Big-O ignores constants

    Big-O is concerned with the overarching categories of algorithmic speeds. O(N) and $$O(N^2)$$ are completely different categories. O(N) grows linearly as the data increases. $$O(N^2)$$ grows exponentially as the data increases. 

    Any factor of N in O(N) will at some data size be faster than $$O(N^2)$$. Hence, these are differentiated in Big-O.

    But, both O(N) and O(100N) grow linearly as the data increases. This does not interest Big-O. Therefore, both of these algorithms are put under the same category of O(N).

    This is why bubble sort and selection sort are both $$O(N^2)$$ even though in reality, selection sort is twice as fast as bubble sort.

# Chapter 6: Optimizing for optimistic scenarios

1. Chapter intent: 

    Big-O focuses on worst-case scenarios. But what about those situations which are not worst-case, rather average-case scenarios. In this chapter we will be focusing on such scenarios. 

1. Insertion sort

    Animation of how this works in [wikipedia](https://en.wikipedia.org/wiki/Insertion_sort#Algorithm).

    1. Big O Notation only takes into account the highest order of N when we have multiple orders added together.

        i.e. $$O(N^2 + 2N - 2) \implies O(N^2 + N) \implies O(N^2)$$

    1. Time complexity of insertion sort

        <ins>In worst case scenarion insertion sort has time complexity of $$O(N^2)$$, the same as bubble sort and selection sort.</ins> 

    1. Efficiency of insertion sort

        - Selection sort: $$O(N^2/2) \implies O(N^2)$$
        - Bubble sort: $$O(N^2) \implies O(N^2)$$
        - Insertion sort: $$O(N^2+2N-2) \implies O(N^2)$$

        Remember these are worst case time complexities. In the average case, insertion sort performs much better. 

    1. Insertion sort v/s selection sort

        ||Best case|Average case|Worst case|
        |-|-|-|-|
        |Selection sort|$$N^2/2$$|$$N^2/2$$|$$N^2/2$$|
        |Insertion sort|N|$$N^2/2$$|$$N^2$$|

# Chapter 7: Big O in everyday code

Exercises worked out [here]({%post_url Common-Sense-DSA/2025-11-02-code-examples-common-sense-dsa%}#chapter-7-big-o-in-everyday-code).

# Chapter 8: Blazing fast lookups with hash tables

1. Rationale for hash tables

    The best time complexity for searching in arrays is the case of ordered arrays where we can use binary search that has O(log N). Hash tables beat this quite considerably by having O(1). 
    
    Searches, reads and insertions in hash tables are O(1).

1. What is a hash table (alias dictionary)

    A hash table is a list of paired values. The first item in each pair is called the key, and the second item is called the value.

1. Hash tables worst case O(N)

    When there are collisions, in the worst case it could be possible that all the entered keys hash to the same index. Then, this index would have multiple subarrays with each subarray having a key at index 0 and value at index 1. In this case, hash tables have same time complexity as arrays since a linear search needs to be done in hash table as well. 

    ![]({%link assets/images/posts/common_sense_dsa/hash_table_collision.png%})

# Chapter 9: Crafting Elegant Code with Stacks and Queues

1. Stacks and queues mostly used to store temporary data. 

1. Abstract data type:

    Stacks and Queues are abstract data types i.e. they can be implemented with Arrays or any other data structure like hash tables under the hood. Stack and Queue are theoretical concepts. 

1. If stack if just constrained array, why use stack at all?

    - Prevent potential bugs. 
    - Data structures like stack gives us a new mental model for tackling problems with the LIFO process. 
    - More elegance.

1. Queues follow FIFO.


# Chapter 10: Recursively Recurse with Recursion

1. Stack overflow

    Recursion uses call stack to keep track of which function needs to be called next. In case of infinite recursion, the computer keeps pushing the same function again and again onto the call stack. This continues until a point is reached where there is no more memory remaining. Then, the computer shuts down the recursion. A stack overflow is said to be reached. 

1. Exercises present [here]({%post_url Common-Sense-DSA/2025-11-02-code-examples-common-sense-dsa%}#ex-4-3)

# Chapter 11: Learning to Write in Recursive

