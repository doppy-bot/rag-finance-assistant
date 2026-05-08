# Premier League League Table Prediction

## Overview
This project predicts the final Premier League league table using historical match data
retrieved from the football-data.org API. A Random Forest model is trained to estimate
match outcome probabilities, which are then used in a Monte Carlo simulation of the
remaining fixtures.

## Methodology
- Data collection via football-data.org API
- Feature engineering using rolling team performance metrics
- Random Forest classifier for match outcome prediction
- Monte Carlo simulation (5,000 runs) for final table probabilities

## Outputs
- Title, Top 4, and Relegation probabilities
- Visualisations of predicted outcomes

## Tools
- Python
- pandas, numpy
- scikit-learn
- matplotlib

## Author
TARUN JENA
