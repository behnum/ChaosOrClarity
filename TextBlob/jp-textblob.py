"""
Sentiment Analysis Script using TextBlob
Version 1.0.0 | Behnam Baharmand
-----------------------------------------

This Python script performs sentiment analysis on a dataset of comments and saves the results in an output CSV file. It uses the TextBlob library, which is a natural language processing library, to determine the polarity and subjectivity of each comment.

Usage:
1. Ensure that the source file (e.g. 'c4-all.csv') exists in the same directory. This file should contain one comment per line.
2. Run this script to analyze the sentiment of the comments.
3. The script will generate an output file (i.e., 'jspa-c4-output.csv') with columns for the original comment, polarity, and subjectivity.

Libraries Used:
- csv: Used for reading and writing CSV files.
- time: Used for measuring the execution time of the script.
- TextBlob: A Python library that provides simple and intuitive tools for processing textual data.

Script Workflow:
1. Import necessary libraries, including 'csv', 'time', and 'TextBlob'.
2. Record the start time to measure the script's execution time.
3. Initialize an empty list 'results_list' to store the analysis results.
4. Open the 'c4-all.csv' file and read its contents into 'dataset_list', removing any line breaks.
5. Iterate through each comment in 'dataset_list' and perform sentiment analysis using 'TextBlob'.
6. Calculate the polarity and subjectivity of each comment.
7. Store the original comment, polarity, and subjectivity in 'results_list'.
8. Print the number of comments processed.
9. Define the export filename as 'jspa-c4-output.csv' and set the header fields for the CSV file.
10. Write the analysis results to the 'jspa-c4-output.csv' file.
11. Calculate and print the script's execution time in seconds.

To Use:
- Place your 'c4-all.csv' file in the same directory as this script.
- Run the script to perform sentiment analysis and generate 'jspa-c4-output.csv'.

"""

import csv
import time
from textblob import TextBlob

# Takes in dataset.csv which is one comment per line.
# Saves output.csv which is original_comment | polarity | sentiment

start_time = time.time()  # Let's see how long it takes to run the code

results_list = []

with open("c4-all.csv", "r", encoding="UTF-8") as inputfile:
    dataset_list = inputfile.readlines()  # list of lines
    dataset_list = list(map(str.strip, dataset_list))  # Remove line breaks

    for item in dataset_list:
        tb = TextBlob(item)
        polarity = round(tb.polarity, 3)
        subjectivity = round(tb.subjectivity, 3)
        results_list.append([item, polarity, subjectivity])

print(len(results_list))

export_filename = "jspa-c4-output.csv"
header_fields = ["Comment", "Polarity", "Subjectivity"]
rows = results_list

with open(export_filename, "w", encoding="UTF-8") as csvfile:
    csvwriter = csv.writer(csvfile)  # Createa csv writer obj
    csvwriter.writerow(header_fields)  # writing the field

    csvwriter.writerows(results_list)  # writing the data rows

print("▐░░ Processs finished in: %s seconds\n" % round((time.time() - start_time), 3))
