# Credit-Risk-Segmentation
Credit risk segmentation using EDA and unsupervised learning on Kaggle data

## Overview
This project performs exploratory data analysis and unsupervised risk segmentation
on customer credit data. Since the dataset does not contain a labeled default variable,
the focus is on identifying risk patterns rather than prediction.

## Dataset
- Source: Kaggle
- Records: 51,336 customers
- Features: Credit exposure, loan mix, missed payments, credit age
- No target variable available
- Dataset Website:- "https://www.kaggle.com/code/mafayed/credit-risk-analysis"

## Methodology
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Correlation analysis
- KMeans clustering (k = 4)
- PCA visualization
- Risk score creation

## Results
Customers were segmented into four groups:
- Low Risk
- Medium Risk
- High Risk
- No Credit History

High-risk segments show higher missed payments and credit exposure,
while thin-file customers form a distinct group.

## Tools Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

## Disclaimer
This project focuses on descriptive risk segmentation and does not perform
credit default prediction due to the absence of labeled outcome data.

## Dataset Source
The dataset used in this project was obtained from Kaggle and is used
strictly for educational and research purposes.
