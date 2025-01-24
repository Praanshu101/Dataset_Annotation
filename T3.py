# Task 3

# Cohen's Kappa for POS tagging

# Make a dictionary for each data point in a csv file ({'word': 'entity'})
# csv file has columns: "annotation_id","annotator","created_at","id","label","lead_time","text","updated_at"
# The "label" column is a list of dictionaries with the keys "start", "end", "label", "text"
# Of these, we are interested in the "text" and "label" keys (These are the words and their corresponding entities)

import csv
import json

# Read the csv file and convert it to a list
def csv_to_dict(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        data = list(reader)
    return data

# Create the list of dictionaries
def create_dict(data):
    lst = []
    for i in range(len(data)):
        # Ensure the row has at least 5 columns (Skipping the blank rows)
        if len(data[i]) > 4:
            dict = {}
            # Extracting the "label" column
            label_str = data[i][4]
            if label_str:  # Checking if label_str is not empty
                # Correcting the JSON string format
                label_str = label_str.replace('""', '"')
                label = json.loads(label_str)
                # From the "label" column, extracting the "text" and "label" keys
                for j in range(len(label)):
                    # Extracting the "text" and "label" keys
                    word = label[j]['text']
                    entity = label[j]['labels'][0]
                    # Creating the dictionary
                    dict[word] = entity
            lst.append(dict)
    return lst

# Print the list of dictionaries
def print_dict(lst):
    for i in range(len(lst)):
        print(lst[i])

# Testing for file NER1.csv
data = csv_to_dict('NER1.csv')
dict = create_dict(data)
print_dict(dict)

# Cohen's Kappa calculation
# The formula for Cohen's Kappa is:
# Kappa = (Po - Pe) / (1 - Pe)

# Comparing with same data for now (dict)

# Po




# Fliess' Kappa 

# Making a list of labels for each image

def create_label_list(data):
    lst = []
    for i in range(len(data)):
        # Ensure the row has at least 5 columns (Skipping the blank rows)
        if len(data[i]) > 4:
            # Extracting the "choice" column
            label = data[i][2]
            lst.append(label)
    return lst

# Print the list of labels
def print_labels(lst):
    for i in range(len(lst)):
        print(lst[i])

# Testing for file CV1.csv

data = csv_to_dict('CV1.csv')
labels = create_label_list(data)
print_labels(labels)
