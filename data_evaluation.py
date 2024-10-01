# 3. data_evaluation.py

import pandas as pd

def evaluate_data(file_path):
    # Load the cleaned data from 'netflix_show_movies.csv'
    df = pd.read_csv(file_path)

    # Select only the relevant columns
    selected_columns = ['type', 'release_year', 'rating', 'duration', 'Recoded_duration', 'Recoded_release_year']
    
    # Filter the DataFrame to include only the selected columns
    df_selected = df[selected_columns]

    # Display the head of the DataFrame
    print("Head of the DataFrame:")
    print(df_selected.head())

    # Display info of the DataFrame once
    print("\nInfo of the DataFrame:")
    df_selected.info()

    # Display summary statistics for the selected columns only
    print("\nSummary statistics of the selected columns:")
    print(df_selected.describe()) 

    # Check for missing values
    missing_values = df_selected.isnull().sum()
    print("\nMissing values in each column:")
    print(missing_values)

    # Check if the data is clean (no missing values)
    if missing_values.any():
        print("\nWarning: Missing values detected in the cleaned data.")
    else:
        print("\nData is clean with no missing values.")

    return df_selected
