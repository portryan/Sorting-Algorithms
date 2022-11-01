import random

def sortList(listA):
    if len(listA) < 1:
        return listA

    for i in range(len(listA)):                                 # O(n) | Loops full length of ListA worst case
        swapped = False                                         # Set swapped to False so it doesnt run forever
        for j in range(len(listA)-i-1):                         # O(n) | Loops length depends on ListA. Each time this loop runs, the highest value(s) will be sent to the back so we can decrease the loop time by i each time. We also subtract 1 since we start at 0 and could go out of bounds at the end with j+1
            if (listA[j] > listA[j+1]):                         # Checks if the current element is greater than the next element
                temp = listA[j]                                 # Creates a temp variable since the current element is about to be overwritten
                listA[j] = listA[j+1]                           # Copy the next element to the current element
                listA[j+1] = temp                               # Set the next element equal to the temp value
                swapped = True                                  # Set swapped equal to True since there has been at least one swap   
        if (swapped == False):                                  # Break the loop if there has been no swaps, this tells us the list is sorted
            break

    return listA                                                # Return sorted list


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

newList = sortList(randomList)

print("ListB =",newList)