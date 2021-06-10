# 18120027_Nguyen Thi Thu Hang
# 18120178_Pham Thi Hoai Hien
# Load the convenient packages
import numpy as np
import pandas as pd
import math

# Load dataset
def getDataset(filename):
    dataset = pd.read_csv(filename)
    return dataset


def getNumberOfInstances(dataset):
    return dataset.shape[0]


def getNumberOfAttributes(dataset):
    return dataset.shape[1]

# get list of attribute in dataset
def list_attributes(dataset):
    return list(dataset)


# To check num is NaN? (1: is NaN, 0: not NaN)
def isNaN(num):
    return num != num or str(num) == " "


# To check each element of array is NaN
def isNaN_Array(array):
    Array = []
    for x in array:
        Array.append(isNaN(x))
    return Array


# get the number of missed data
def list_NumberOfMissing(dataset):
    NumberOfMissing = {}  # constaint attribute and number of missing data
    attributes = list_attributes(dataset)  # get list of Attribute
    NumOfInstances = getNumberOfInstances(dataset)  # get the number of Instances
    for attribute in attributes:  # Check each of attributes
        MissingArray = isNaN_Array(dataset[attribute])  # IsNaN ~ 1      NotIsNaN ~ 0
        NumOfMiss = 0
        for index in range(NumOfInstances):
            NumOfMiss += int(MissingArray[index])
        NumberOfMissing[attribute] = NumOfMiss
    return NumberOfMissing


# get MEANS value of Array
def MEANS(array):
    sum = 0
    NumOfValues = 0
    Array = isNaN_Array(array)
    for i in range(array.shape[0]):
        if (Array[i] == False):
            sum += array[i]
            NumOfValues += 1
    return round((sum / NumOfValues), 3)


# get MEDIAN value of Array
def MEDIAN(array):
    Array = isNaN_Array(array)
    ValuesOfArray = []
    for i in range(array.shape[0]):
        if (isNaN(array[i]) == False):
            ValuesOfArray.append(array[i])
    ValuesOfArray.sort()
    N = int(len(ValuesOfArray) / 2)
    if (N % 2 == 0):
        return (ValuesOfArray[N - 1] + ValuesOfArray[N]) / 2
    else:
        return ValuesOfArray[N]


# get MODE value of Array
def MODE(array):
    ValueOfArray = {}
    Array = isNaN_Array(array)
    for i in range(array.shape[0]):
        if (isNaN(array[i]) == False):
            if array[i] in ValueOfArray:
                ValueOfArray[array[i]] += 1
            else:
                ValueOfArray[array[i]] = 1
    max = 0
    result = ''
    for Values in ValueOfArray:
        if (max < ValueOfArray[Values]):
            max = ValueOfArray[Values]
            result = Values
    return result


# find Type of Attributes
# convention:
# type = 1 : int or int64
# type = 2 : float or float64
# type = 3 : nominal
# type = 4: Number Of Missing Data equal Number Of Instances
def getTypeOfAttributes(dataset):
    TypeOfAttributes = {}  # constaint attribute and type of data
    attributes = list_attributes(dataset)  # get list of Attribute
    NumberOfMissing = list_NumberOfMissing(dataset)  # get the number of missed data
    NumOfInstances = getNumberOfInstances(dataset)
    for attribute in attributes:
        if (NumberOfMissing[attribute] == NumOfInstances):
            TypeOfAttributes[attribute] = 4 #NULL attribute
            continue
        for index in range(NumOfInstances):
            if (isNaN(dataset[attribute][index]) == False):
                if (type(dataset[attribute][index]) == int or type(dataset[attribute][index]) == np.int64):
                    TypeOfAttributes[attribute] = 1 #int attribute                    
                elif (type(dataset[attribute][index]) == float or type(dataset[attribute][index]) == np.float64):
                    TypeOfAttributes[attribute] = 2 #float attribute                    
                else:
                    TypeOfAttributes[attribute] = 3 #nominal attribute                    
                break
    return TypeOfAttributes
