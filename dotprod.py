"""
File: dotprod.py
Author: James Lawson
"""

import numpy as np
import random
import time
import matplotlib.pyplot as plt

# Dot Product Function - stack overflow linked that helped me: 
# https://stackoverflow.com/questions/32669855/dot-product-of-two-lists-in-python

def dotProduct(a, b):
    return sum(i[0] * i[1] for i in zip(a, b))

if __name__ == "__main__":    
    # 2 lists are created
    a = []
    b = []
    
    # 1 million elements are added to both of the lists
    for k in range(1000000):
        a.append(random.random())
        b.append(random.random())
    
    # Lists are convered to a NumPy array
    a = np.asarray(a)
    b = np.asarray(b)
    
    # Takes start time
    startTime = time.time()
    
    # Calls the dot product function
    dotProduct = dotProduct(a,b)
    
    # Takes end time
    endTime = time.time()
    
    # Total time is calculated and rounded
    totalTime = endTime - startTime
    totalTime = round(totalTime, 5)
    
    
    # Prints the NP dot product
    dotProduct = round(dotProduct, 5)
    print("We expect the result to be ~250,000, a quarter of 1 million values in each NumPy array")
    print("The dot product is: ", dotProduct)

    # Takes start time
    startTimeNP = time.time()
    
    # Calls the NP dot product function
    dotProductNP = np.dot(a,b)
    
    # Takes end time
    endTimeNP = time.time()
    
    # Prints the NP dot product
    dotProductNP = round(dotProductNP, 5)
    print("The dot product calculated using NP is: ", dotProductNP)
    
    # Total time is calculated, rounded, and printed
    totalTimeNP = endTimeNP - startTimeNP
    totalTimeNP = round(totalTimeNP, 5)
    print("The time taken by the dot-product calculation is: ", totalTime)
    print("The time taken by the NP dot-product function is: ", totalTimeNP)
    
    # Part 3 ----------------------------------------------------------------
    
    # 2 NumPy arrays are created to store values
    a = np.array([])
    b = np.array([])
    
    # 2 empty numpy arrays are initialized
    rollYourOwn = np.array([])
    NumPy = np.array([])
    
    print("Creating Visualization......................")
    
    # Step 10 times from 10,000 to 100,000 in increments of 10,000
    for x in range(10):
        # 10,000 random values are added to the empty numpy arrays
        for k in range(10000):
            a = np.append(a, random.random())
            b = np.append(b, random.random())
        
        # Takes start time
        startTime = time.time()
    
        # Calculates the dot product
        dotProduct = sum(i[0] * i[1] for i in zip(a, b))
    
        # Takes end time
        endTime = time.time()
    
        # Total time is calculated and rounded
        totalTime = endTime - startTime
        totalTime = round(totalTime, 5)
        
        # Append the time to the empty array
        rollYourOwn = np.append(rollYourOwn, totalTime)

        #-------------------------------------------------------

        # Takes start time
        startTimeNP = time.time()
    
        # Calls the NP dot product function
        dotProductNP = np.dot(a,b)
    
        # Takes end time
        endTimeNP = time.time()
    
        # Total time is calculated and rounded
        totalTimeNP = endTimeNP - startTimeNP
        totalTimeNP = round(totalTimeNP, 5)
        
        # Append the time to the empty array
        NumPy = np.append(NumPy, totalTimeNP)
        
    # Numpy arrays are printed
    print("Roll Your Own Times: ", rollYourOwn)
    print("NumPy Times: ", NumPy)
    
    # Graph Visualization is created
    # linked that helped me - https://www.sitepoint.com/plot-charts-python-matplotlib/
    plt.plot(rollYourOwn, label="Roll Your Own")
    plt.plot(NumPy, label="NumPy")
    plt.title("Time Taken: Roll Your Own vs. NumPy")
    plt.xlabel("Number of Values")
    plt.ylabel("Time (sec)")
    plt.legend(loc="best")
    plt.show()