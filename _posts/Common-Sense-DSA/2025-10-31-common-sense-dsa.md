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

# Speeding up your code with Big O

1. Bubble sort

    In each pass through, the highest unsorted value "bubbles" up to its correct position. 

    Bubble sort has $$ O(N^2) $$ complexity. This means bubble sort has *quadratic time*.