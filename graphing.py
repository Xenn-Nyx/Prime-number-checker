'''
    graphing.py
    Created by Xenn_Nyx on 13/7/23
    Graphs prime numbers found in the main.py file
    
    Inputs: primes (list)
    Outputs: graph
'''


##import necessary modules
import matplotlib.pyplot as plt
##actual function
def graphing(primes: list):
    '''
        graphing.py
        Created by Xenn_Nyx on 13/7/23
        Graphs prime numbers found in the main.py file
        
        Inputs: primes (list)
        Outputs: graph
    '''
    #Initialise some variables
    xVals=[]
    position=1
    yVals=primes

    #create an array for the index of prime numbers
    while position<=len(primes):
        xVals.append(position)
        position+=1
    #do the graphing thing

    #first plot values against index,
    plt.subplot(2,1,1)
    plt.xlabel("Index")
    plt.ylabel("Value of prime")
    plt.title("Primes vs Index")
    plt.plot(xVals, yVals, c='darkslategrey')

    #then plot values for all numbers (number system plot)
    plt.subplot(2,1,2)
    plt.xlabel("Numbers")
    plt.ylabel("Value of prime")
    plt.title("Primes in Context")
    plt.scatter(yVals, yVals, c='darkslategrey')

    #show the result
    plt.show()