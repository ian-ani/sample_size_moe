# PYTHON VERSION: 3.12.7

import math
import os
import json


# p is standard deviation from population
# needed for both sample size and margin of error
# when unknown is 0.50 by default
P = 0.50


# ------------------------------------
# For sample size and margin of error
# ------------------------------------

# Asks for population size
def ask_population_size(population_size):
    if population_size == "":
        population_size = 0

    try:
        float(population_size)
    except ValueError:
        print(f"Error: {population_size} is not a number.")
        population_size = 0

    return population_size


# Asks level of confidence
def ask_confidence(confidence):
    if confidence == "":
        confidence = 0

    try:
        float(confidence)
    except ValueError:
        print(f"Error: {confidence} is not a number.")
        confidence = 0

    return confidence


# Gets zscore value after asking for level of confidence
def get_zscore(confidence):
    if confidence == "":
        confidence = 0

    folder = "zscore_table"
    filename = "table.json"
    path_dict = os.path.join(folder, filename)
    
    with open(path_dict, "r", encoding="utf-8") as file:
            zscore_table = json.load(file)

    try:
        zscore_value = zscore_table["zscore"]
        return zscore_value[confidence]
    except KeyError:
        print(f"Error: can't find {confidence} in the zscore table, try an integer between 1 and 99.")
    

# ------------------
# For sample size
# ------------------

# Asks for margin of error
def ask_margin_error(decimal_margin_error):
    if decimal_margin_error == "":
        decimal_margin_error = 0

    try:
        float(decimal_margin_error)
    except ValueError:
        print(f"Error: {decimal_margin_error} is not a number.")
        decimal_margin_error = 0
 
    margin_error = float(decimal_margin_error) / 100

    return margin_error


# Returns sample size
def calculate_sample_size(population_size, z_score, margin_error):
    if z_score is None:
        z_score = 0

    try:
        sample_size = float(z_score)**2 * P * (1 - P) / (float(margin_error)**2 + (float(z_score)**2 * P * (1 - P)) / int(population_size))
        rounded_size = math.ceil(sample_size)
        return rounded_size
    except ZeroDivisionError:
        print(f"Error: can't divide by zero.")


# --------------------
# For margin of error
# --------------------

# Asks for sample size
def ask_sample_size(sample_size):
    if sample_size == "":
        sample_size = 0

    try:
        float(sample_size)
    except ValueError:
        print(f"Error: {sample_size} is not a number.")
        sample_size = 0

    return sample_size


# Returns margin of error
def calculate_margin_error(population_size, z_score, sample_size):
    if z_score is None:
        z_score = 0

    try:
        margin_error = float(z_score) * math.sqrt(P * (1 - P)) / math.sqrt((int(population_size) - 1) * int(sample_size) / (int(population_size) - int(sample_size)))
        percentage_margin = margin_error * 100
        rounded_margin = round(percentage_margin, 2)
        return rounded_margin
    except ZeroDivisionError:
        print(f"Error: can't divide by zero.")
