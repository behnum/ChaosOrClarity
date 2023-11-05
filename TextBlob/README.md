# Sentiment Analysis Script using TextBlob

## Overview

This Python script performs sentiment analysis on a dataset of comments and saves the results in an output CSV file. It uses the TextBlob library, a natural language processing tool, to determine the polarity and subjectivity of each comment.

## Usage

1. Ensure that the source file (e.g. 'c4-all.csv') exists in the same directory. This file should contain one comment per line.
2. Run this script to analyze the sentiment of the comments.
3. The script will generate an output file (i.e., 'jspa-c4-output.csv') with columns for the original comment, polarity, and subjectivity.

## Libraries Used

- `csv`: Used for reading and writing CSV files.
- `time`: Used for measuring the execution time of the script.
- `TextBlob`: A Python library for natural language processing, used for sentiment analysis.

## Script Workflow

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

## Getting Started

- Place your 'c4-all.csv' file in the same directory as this script.
- Run the script to perform sentiment analysis and generate 'jspa-c4-output.csv'.
