## Internship project at Elietch

## Project Overview
This repository contains solutions for all four tasks of the EliteTech  Internship Program, focusing on data analysis, machine learning, dashboard development, and NLP.

**Task 1: Big Data Analysis**

Analyze a dataset to explore the global impact of AI on factors like adoption rates, job loss due to AI, and revenue increases due to AI.

**Task 2: Predictive Modeling**

Use Random Forest Regressor to predict the revenue increase based on factors like AI adoption rate and job loss predictions.

**Task 3: Interactive Dashboard**

Create an interactive web dashboard using Dash. This dashboard allows users to filter data by year and industry and visualize various metrics like AI adoption, job impacts, and revenue increase.

**Task 4: Sentiment Analysis**

Perform sentiment analysis on the Regulation Status column using VADER Sentiment Analysis from the NLTK library. The sentiment analysis is visualized and correlated with consumer trust in AI.


## Features
**Data Cleaning:** Handles missing values in the dataset to ensure accuracy.

**Predictive Modeling:** A machine learning model to predict revenue increases from AI adoption.

**Interactive Dashboard:** A real-time, interactive web application built using Dash to visualize key data points.

**Sentiment Analysis:** Analyzes sentiment scores for regulatory statuses and explores their impact on consumer trust.


## Requirements

Before running the project, you need to install the following dependencies:

Python 3.x

Libraries:

pandas

matplotlib

seaborn

plotly

dash

scikit-learn

nltk

pyspark

To install these libraries, use the following command:

**pip install pandas matplotlib seaborn plotly dash scikit-learn nltk pyspark**

## Dashboard Server Setup

**Start the Server:** The interactive dashboard is powered by Dash. 

To start the server, navigate to the project directory and run: **python dashboard_app.py**

**Automatically Open Browser**: When the server starts, the application will automatically open in your default web browser. You can also open the dashboard manually by visiting the above URL.
![Uploading image.png…]()


**Interactive Features:**

**Year Selector:** Select one or multiple years to view the data for those specific years.

**Industry Selector:** Filter the data by industry to see the impact of AI on different sectors.

**Dynamic Visualizations:** The dashboard will update visualizations like heatmaps, scatter plots, and bar charts based on the selected filters.


## Visualizations

**Sentiment Distribution:** A histogram showing the distribution of sentiment scores for regulations across countries.

**Sentiment vs Consumer Trust:** A scatter plot that visualizes the correlation between regulation sentiment and consumer trust in AI.

**Sentiment by Industry:** A box plot comparing the sentiment of regulations across different industries.

**AI Adoption and Revenue Impact:** Visualizations showing the relationship between AI adoption rates and revenue increases.

## Conclusion
This project combines data exploration, machine learning, sentiment analysis, and interactive visualizations to analyze the global impact of AI. The interactive dashboard allows users to explore and filter the data dynamically, while the predictive model provides insights into the future impact of AI on revenue.



