# Fairness-Bias-Income-Prediction
Fairness and bias analysis in income prediction using the Adult Census dataset

## Overview
This project analyzes fairness and bias in an income prediction model using the Adult Census Income dataset.
The objective is to evaluate demographic disparities in model outcomes rather than maximize predictive accuracy.

## Dataset
- Adult Census Income Dataset
- Source: Kaggle
- Target: Income (>50K / ≤50K)

The dataset is not included in this repository due to licensing considerations.

## Methodology
- Data cleaning and preprocessing
- Bias-aware exploratory data analysis (EDA)
- Baseline Logistic Regression model
- Fairness evaluation using:
  - Demographic Parity
  - Disparate Impact Ratio
  - Equal Opportunity
- Intersectional bias analysis (Gender × Race)

## Key Findings
- Significant income disparities exist across gender and race in the data.
- Model predictions show unequal selection rates across demographic groups.
- True Positive Rates differ across groups, indicating opportunity disparities.
- Intersectional analysis reveals compounded disadvantage for certain groups.

## Visualizations
(See images folder for plots)

## Ethical Considerations
- Observed disparities may reflect historical and societal inequalities.
- Fairness metrics indicate outcome differences, not intent or causality.
- Removing sensitive attributes alone does not guarantee fairness due to proxy variables.

## Disclaimer
This project is for educational and research purposes only and does not represent a production-ready system.
