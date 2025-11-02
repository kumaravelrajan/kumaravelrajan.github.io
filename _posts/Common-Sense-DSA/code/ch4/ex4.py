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