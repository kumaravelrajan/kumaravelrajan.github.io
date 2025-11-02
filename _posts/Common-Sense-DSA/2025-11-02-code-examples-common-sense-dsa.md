---
hidden: true
categories: 

    - cs
    - programming
    - dsa

description: My code for the exercises of the book Common sense DSA by Jay Wengrow. 
---

# Chapter 4: Speeding up your code with Big O

## Exercise 4_4
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