'''
    Main.py
    Created by Xenn_Nyx on 25/6/23
    Interfaces with prime_check.py to check for prime in a certain specified range
    
    Inputs: none externally (self-generated console inputs)
    Outputs: console statements

    Features a silent mode for suppressed console outputs until the end
'''
##Import needed modules
from prime_check import prime_check as prime

##Data validation
while True:
    #first get an input from the user for range, silent mode enable
    userRange=input("Enter a range of values to check for (in the format x-y):\n")
    silentMode=input("Would you like to run in silent mode (0/1): ")
    #Ensure correct format
    try:
        userVals=userRange.split('-')
        startVal=int(userVals[0])
        endVal=int(userVals[1])
        if startVal>=endVal:
            print("Error: Start value > ending value!")
            continue
        silentMode=bool(int(silentMode))
        #tell the user their inputs (to double check)
        print(f"Starting value is {startVal}")
        print(f"Ending value is {endVal}")
        break
    #if not in correct format, tell the user, get inputs again
    except:
        print("Unexpected input!")

##Do the thing, you know, the thing
#Print a message displaying that the program is now working
print(f"Checking for primes between {startVal} and {endVal}. Please be patient...")

incrementor=startVal
primeArray=[]
while incrementor<endVal:
    currentVal=prime(incrementor,silentMode)
    if currentVal != None:
        primeArray.append(currentVal)
    incrementor+=1
print(primeArray)