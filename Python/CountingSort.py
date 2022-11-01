import random
                                                                # List A = original array, List B = sorted array, List C = counting array
                                                                # n = number of items in original list, k = range of values
def sortList(listA, lower, upper):
    listSize = len(listA)                                       # Gets the size of the original unsorted list
    rangeOfValues = upper-lower
    listB = [0 for i in range(listSize)]                        # Initializes List B with size of the original list
    listC = [0 for i in range(rangeOfValues+1)]                 # Initializes List C with the size of the range between values, +1 since its inclusive
    
    for i in range(listSize):                                   # O(n) | Counts how many times a value appears in List A, and places that amount in List C with the appropiate index
        index = listA[i]-lower                                  # Gets the index based off the difference of the value minus the lower bound
        listC[index] = listC[index] + 1                         # Adds 1 to the count in List C for that value
    
    if len(listC) > 0:                                          # Only run if List C > 0 since it could go out of bounds
        for i in range(1,len(listC)):                           # O(k) | Runs length of List C - 1 times, starts at index 1
            listC[i] = listC[i] + listC[i-1]                    # Add current value in List C to the value in the previous index
    else:
        return listA                                            # Return the original list if List C <= 0, there is no point continuing since the range is 0

    for i in range(listSize):                                   # O(n) | Runs the size of List A times since List B has the same size 
        valA = listA[(listSize-1)-i]                            # Get the value in List A, starting at the end
        indexC = listC[valA - lower]                            # Get the index of the value in List C
        listB[indexC-1] = valA                                  # Put the value from List A in List B
        listC[valA - lower] = listC[valA - lower] - 1           # Subtract 1 from the value in List C
    return listB

listSize = int(input(("How many random numbers? ")))
lowerBound = int(input("Lowest number? "))
upperBound = int(input("Highest number? "))
#listSize = 100
#lowerBound = 1
#upperBound = 50

randomList = []

for i in range(listSize):                                        # Generate list of random numbers based off user input
    num = random.randint(lowerBound, upperBound)
    randomList.append(num)

print("ListA =",randomList)

newList = sortList(randomList, lowerBound, upperBound)          # Counting Sort requires to know the lower and upper bound of values

print("ListB =",newList)