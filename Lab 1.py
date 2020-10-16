#Kyle Johnson
#Algorithms 9:00 AM
#10-16-20
#Prof. Skaggs

import math
import itertools

#I didn't use these but just brushed up on recursion with them
def factorial(n):
  if(n > 0):
    result = n * factorial(n - 1)
  else:
    result = 1
  return result

def plus_or_minus_one(n):
    if(n % 2 == 0):
        return 1
    else:
        return -1

def derangements_1(n):
    if(n > 1):
        result = (n * derangements_1(n-1) + math.pow(-1, n))
    else:
        result = 0
    return int(math.floor(result))

def derangements_2(n):
    return math.floor( ((math.factorial(n)) / (math.exp(1))) + (1/2) )

def derangements_3(n):
    if(n > 1):
        result = ((n-1) * ( derangements_4(n-1) + derangements_4(n-2) ) )
    else:
        result = 0
    return result

def derangements_4(n):
    if(n == 0):
        return 1
    elif(n == 1):
        return 0
    else:
        originalList = create_list(n)
        permutationList = list(itertools.permutations(originalList))
        #print(originalList)
        #print(permutationList)
        i = 0
        x = 0
        derangementCounter = 0
        while( x < len(permutationList)):
            while( i < n):
                if(permutationList[x][i] != originalList[i]):
                    #print("mismatch keep going")
                    i += 1
                else:
                    #print("match dont increment but reset")
                    i = 0
                    x += 1
                if( (i) == len(originalList)):
                    #print("=================increment!==========================")
                    i = 0
                    x += 1
                    derangementCounter+=1
                if( x == len(permutationList)):
                    break
    return derangementCounter 

def create_list(n):
    if n == 1:
        return [1]   # base case, still returns a list

    lst = create_list(n-1)
    refactorList = lst[-1] + 1
    lst.append(refactorList)
    return lst

val = input("Enter a number for the given amount of permutations to calculate the derangements: ")
print("Derangements 1 based on our guess:")
print(derangements_1(int(val)))
print("Derangements 2 based inclusion and exclusion:")
print(derangements_2(int(val)))
print("Derangements 3 given 2 different possibilities of appearances for the value (secret santa/ peer grading):")
print(derangements_3(int(val)))
print("Derangements 4 based on counting:")
print(derangements_4(int(val)))