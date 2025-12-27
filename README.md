# Carbon Emissions Prediction

This project predicts global CO₂ emissions using Machine Learning and visualizes historical emission trends using an interactive Streamlit dashboard.

## Dataset
The dataset used is from **Our World in Data**:
https://github.com/owid/co2-data

Key features used:
- Year
- Population
- GDP
- CO₂ emissions

## Machine Learning Model
A **Random Forest Regressor** is used to predict CO₂ emissions based on historical trends and economic indicators.

## Trained Model File
The trained model exceeded GitHub’s 25 MB file size limit.
Therefore, it has been uploaded as split ZIP files:

- co2_rf_model.zip.001  
- co2_rf_model.zip.002  
- co2_rf_model.zip.003  

### How to restore the model
1. Download all ZIP parts
2. Right-click → Extract Here using 7-Zip
3. This recreates `co2_rf_model.pkl`

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- Matplotlib

## Author
Project created for academic submission.
