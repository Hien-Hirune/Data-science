"""
    Argument syntax:
        python delete_missing_col.py input.csv --missing_rate=missing_rate --output=output.csv
    Example:
        python3 delete_missing_col.py hawks.csv --missing_rate=60 --output=hawks.csv
"""

# Load the convenient packages
import sys

from SupportFunction import getDataset, getNumberOfInstances, list_attributes, list_NumberOfMissing

input = sys.argv[1]
missing_rate = int(sys.argv[2].split("=")[1]) / 100
output = sys.argv[3].split("=")[1]

# get dataset
dataset = getDataset(input)
NumberOfInstances = getNumberOfInstances(dataset)
NumberOfMissing = list_NumberOfMissing(dataset)
attributes = list_attributes(dataset)

missing_threshold = missing_rate*NumberOfInstances

for attribute in attributes:
    if (NumberOfMissing[attribute] > missing_threshold):
        print(attribute, 'missing ', NumberOfMissing[attribute])
        del dataset[attribute]

dataset.to_csv(output, index=False)
