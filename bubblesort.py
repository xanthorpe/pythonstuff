import random
import timeit

def bubbleSort(inputList):
    if(len(inputList) == 1):
        return inputList

    for i in range(0,len(inputList)):
        for j in range(0,len(inputList)-1):
            if(inputList[j][1] > inputList[j+1][1]):
                inputList[j], inputList[j+1] = inputList[j+1], inputList[j]
    return inputList
final_data = []
f = open("nameprioritiessmall.txt", "r")
split_data = f.read().strip().split("\n")
for i in split_data:
    x = i.split(",")
    for j in x:
        y = int(x[1])
        final_data.append(y)
print(final_data)
