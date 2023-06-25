import math
import time
def prime_check(num,silentMode):
    try:
        num=int(str(num))
        silentMode=bool(silentMode)
    except:
        print("Number not an int...")
    maxCheck=math.ceil(num/2)
    if num==1:
        if silentMode==False:
            print("1 is prime")
        return num
    if num==2:
        if silentMode==False:
            print("2 is prime")
        return num
    if num%2==0:
            if silentMode==False:
                print(f"{num} is not a prime")
            return None
    for check in range(3,maxCheck+1,2):
        if num%check==0:
            if silentMode==False:
                print(f"{num} is not a prime")
            return None
    if silentMode==False:
        print(f"{num} is prime")
    return num

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