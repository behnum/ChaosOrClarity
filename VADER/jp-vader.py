"""
Sentiment Analysis Script using VADER
Version 1.1.0 | Behnam Baharmand
-----------------------------------------

This Python script performs sentiment analysis on a dataset of comments and saves the results in an output CSV file. It uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool to determine the polarity of each comment.

Usage:
1. Ensure that the source file (e.g. 'c4-all.csv') exists in the same directory. This file should contain one comment per line.
2. Run this script to analyze the sentiment of the comments.
3. The script will generate an output file (i.e.,'c4-all-output.csv') with columns for the original comment, overall sentiment, and compound score.

Libraries Used:
- csv: Used for reading and writing CSV files.
- time: Used for measuring the execution time of the script.
- vaderSentiment: A Python library that provides sentiment analysis using the VADER algorithm.

Dependencies:
- You need to have the 'vaderSentiment' library installed in your Python environment. You can install it using 'pip install vaderSentiment'.

Script Workflow:
1. Import necessary libraries, including 'csv', 'time', and 'vaderSentiment'.
2. Record the start time to measure the script's execution time.
3. Initialize an empty list 'results_list' to store the analysis results.
4. Create a 'SentimentIntensityAnalyzer' object called 'sid_obj' for sentiment analysis.
5. Open the 'c4-all.csv' file and read its contents into 'dataset_list', removing any line breaks.
6. Iterate through each comment in 'dataset_list' and perform sentiment analysis using 'sid_obj'.
7. Determine the overall sentiment of each comment based on the compound score:
    - 'PO' for positive if compound score >= 0.05
    - 'NE' for negative if compound score <= -0.05
    - 'nu' for neutral otherwise
8. Store the original comment, overall sentiment, and compound score in 'results_list'.
9. Print the number of comments processed.
10. Define the export filename as 'c4-all-output.csv' and set the header fields for the CSV file.
11. Write the analysis results to the 'c4-all-output.csv' file.
12. Calculate and print the script's execution time in seconds.

To Use:
- Ensure 'vaderSentiment' is installed in your Python environment.
- Place your 'c4-all.csv' file in the same directory as this script.
- Run the script to perform sentiment analysis and generate 'c4-all-output.csv'.

"""

import csv
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Takes in dataset.csv which is one comment per line.
# Saves output.csv which is original_comment | polarity | sentiment

start_time = time.time()  # Let's also see how long it takes to run the code

results_list = []

# Create a SentimentIntensityAnalyzer object.
sid_obj = SentimentIntensityAnalyzer()

with open("c4-all.csv", "r", encoding="UTF-8") as inputfile:
    dataset_list = inputfile.readlines()  # list of lines
    dataset_list = list(map(str.strip, dataset_list))  # Remove line breaks

    for item in dataset_list:
        sentiment_dict = sid_obj.polarity_scores(item)

        # decide sentiment as positive, negative and neutral
        if sentiment_dict["compound"] >= 0.05:
            overall_sentiment = "PO"

        elif sentiment_dict["compound"] <= -0.05:
            overall_sentiment = "NE"

        else:
            overall_sentiment = "nu"

        results_list.append([item, overall_sentiment, sentiment_dict["compound"]])

print(len(results_list))

export_filename = "c4-all-output.csv"
header_fields = ["Comment", "overall_sentiment", "compound_score"]
rows = results_list

with open(export_filename, "w", encoding="UTF-8") as csvfile:
    csvwriter = csv.writer(csvfile)  # Createa csv writer obj
    csvwriter.writerow(header_fields)  # writing the field
    csvwriter.writerows(results_list)  # writing the data rows

print("▐░░ Processs finished in: %s seconds\n" % round((time.time() - start_time), 3))
