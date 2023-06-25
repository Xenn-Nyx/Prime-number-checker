'''
    prime_check.py
    Created by Xenn_Nyx on 25/6/23
    Checks for a prime number when input
    
    Inputs: num (integer), silentMode (boolean)
    Outputs: console statements, value (if prime), none otherwise

    Features a silent mode for suppressed console outputs until the end
'''

##import necessary modules
import math
import time

##actual function
def prime_check(num: int, silentMode: bool):
    '''
        prime_check.py
        Created by Xenn_Nyx on 25/6/23
        Checks if input is a prime number
        
        Inputs: num (integer), silentMode (boolean)
        Outputs: console statements, value (if prime), none otherwise

        Incorporates some speed improvements:
            Evens are checked first, and only by dividing by 2 (filters even numbers w/ less instructions)
            Odd divisors are then checked (incrementing to the next odd number)
    '''

    #Validate the data formats
    try:
        num=int(str(num))
        silentMode=bool(silentMode)
    #notify user if number is not an int
    except:
        print("Number not an int...")
    #Calc the max value need to check
    maxCheck=math.ceil(num/2)
    
    #Check if any checks will incorrectly return a prime as non-prime (1,2)
    if num==1:
        if silentMode==False:
            print("1 is prime")
        return num
    if num==2:
        if silentMode==False:
            print("2 is prime")
        return num
    
    #Check for even (all are / by 2)
    if num%2==0:
            if silentMode==False:
                print(f"{num} is not a prime")
            return None
    
    #Check if divisible by an odd number
    for check in range(3,maxCheck+1,2):
        if num%check==0:
            if silentMode==False:
                print(f"{num} is not a prime")
            return None
    #print the value to the console if needed
    if silentMode==False:
        print(f"{num} is prime")
    return num

##Testing code
if __name__=='__main__':
    timeStart=time.time()
    listPrimes=[]
    for i in range(1,10000000,1):
        check=prime_check(i,True)
        if check!=None:
            listPrimes.append(check)
    timeComplete=time.time()-timeStart
    for i in range(0,len(listPrimes)):
        print(f"{listPrimes[i]} is prime!")
    print(f"Time to complete: {timeComplete} seconds")