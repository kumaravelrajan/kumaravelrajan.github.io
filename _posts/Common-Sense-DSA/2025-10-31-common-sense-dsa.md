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

