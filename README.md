# Bike Sharing Analysis Dashboard

This project provides a dashboard to upload and analyze bike sharing data, offering descriptive statistics and visualizations for day-based and hour-based data.

## Features 

- Upload CSV files for day and hour data.
- Display data in table format.
- Perform descriptive statistical analysis.
- Visualize bike usage data based on weather and hour.

## Requirements

- Python 3.9
- Conda 

## Installation Steps

1. **Create a conda environment:**

   ```bash
   conda create --name main-ds python=3.9
   conda activate main-ds

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Direct to the dashboard files**

   ```bash
   cd dashboard
   
4. **Run the dashboard:**

   ```bash
   streamlit run dashboard.py

## How to use the Dashboard
- Open the URL displayed in the terminal after running the streamlit run command.
- On the dashboard, you will see two options to upload CSV files, one for day data and one for hour data. 
- Click the "Browse" button and select the appropriate CSV file from */submission/dashboard/day_data.csv* and */submission/dashboard/hour_data.csv*
- Once the files are uploaded, the data from each file will be displayed in table format.
- You can select the type of analysis you want to perform (Descriptive Statistics or Visualization) using the provided dropdown.
- The results of the analysis (descriptive statistics or visualization) will be displayed below the selection.

## Hosted Dashboard
You can also access the dashboard using this link: **https://bike-dxvnee.streamlit.app/**

