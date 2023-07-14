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
def prime_check(num: int, silentMode: bool, primeList:list):
    '''
        prime_check.py
        Created by Xenn_Nyx on 25/6/23
        Checks if input is a prime number
        
        Inputs: num (integer), silentMode (boolean), primeList (list)
        Outputs: console statements, value (if prime), none otherwise

        Incorporates some speed improvements:
            Only prime numbers are used to check if the number is prime
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
    #check for 1 (causes issues, is not prime by definition)
    if num==1:
        return None
    
    #Check if any checks will incorrectly return a prime as non-prime (2)
    if num==2:
        if silentMode==False:
            print("2 is prime")
        return num
    
    ##New algo
    #as all primes are not divisible by any previous prime number, and all composite numbers are
    #divisible by primes,  the process time is reduced a lot
    for incrementor in range(0,len(primeList)-1):
        #check if the current number is evenly divisible by a prime number
        if num%primeList[incrementor]==0:
            #print the staus if needed
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