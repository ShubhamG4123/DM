import csv
import math

def load_data(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def calculate_entropy(data, class_column):
    class_counts = {}
    for row in data:
        class_value = row[class_column]
        class_counts[class_value] = class_counts.get(class_value, 0) + 1

    entropy = 0
    for count in class_counts.values():
        probability = count / len(data)
        entropy -= probability * math.log2(probability)

    return entropy

def calculate_gini_index(data, class_column):
    class_counts = {}
    for row in data:
        class_value = row[class_column]
        class_counts[class_value] = class_counts.get(class_value, 0) + 1

    gini_index = 1
    for count in class_counts.values():
        probability = count / len(data)
        gini_index -= probability ** 2

    return gini_index

def calculate_gain(data, attribute, class_column):
    total_entropy = calculate_entropy(data, class_column)

    attribute_entropy = 0
    attribute_values = set(row[attribute] for row in data)

    for value in attribute_values:
        subset = [row for row in data if row[attribute] == value]
        subset_entropy = calculate_entropy(subset, class_column)
        weight = len(subset) / len(data)
        attribute_entropy += weight * subset_entropy

    information_gain = total_entropy - attribute_entropy
    return information_gain

def calculate_gini_gain(data, attribute, class_column):
    total_gini = calculate_gini_index(data, class_column)

    attribute_gini = 0
    attribute_values = set(row[attribute] for row in data)

    for value in attribute_values:
        subset = [row for row in data if row[attribute] == value]
        subset_gini = calculate_gini_index(subset, class_column)
        weight = len(subset) / len(data)
        attribute_gini += weight * subset_gini

    gini_gain = total_gini - attribute_gini
    return gini_gain

# Load data from CSV
file_path = 'exp12/data12.csv'  # Replace with your CSV file path
data = load_data(file_path)

class_column_name = 'PlayGame'

# Calculate information gain for each attribute
information_gains = {}
for attribute in data[0].keys():
    if attribute != class_column_name:
        gain = calculate_gain(data, attribute, class_column_name)
        information_gains[attribute] = gain

# Identify the attribute with the maximum information gain
max_gain_attribute = max(information_gains, key=information_gains.get)

# Calculate Gini index for the attribute with the maximum information gain
max_gain_gini_index = calculate_gini_index(data, max_gain_attribute)

# Print information gain of each attribute
print("Information Gain for Each Attribute:")
for attribute, gain in information_gains.items():
    print(f"{attribute}: {gain}")

print(f"\nFor Attribute with Maximum Information Gain ('{max_gain_attribute}'):")
print(f"Information Gain: {information_gains[max_gain_attribute]}")
print(f"Gini Index: {max_gain_gini_index}")
