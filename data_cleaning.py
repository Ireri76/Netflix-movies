# 2. data_cleaning.py

import pandas as pd

def clean_data(df):
    # Calculate the total number of missing values for specific columns
    missing_values = df[['type', 'release_year', 'rating', 'duration']].isnull().sum()
    
    # Calculate the percentage of missing values for specific columns
    total_rows = df.shape[0]
    missing_percentage = (missing_values / total_rows) * 100
    
    # Check if any specified column has more than 5% missing values
    if missing_percentage.any() > 5:
        print("More than 5% missing data found. Proceeding with multiple imputation.")
        
    else:
        print("Missing data is less than or equal to 5%. Dropping rows with missing values.")
        df = df.dropna(subset=['type', 'release_year', 'rating', 'duration']).copy()  
        
    # Create the Recoded_duration column
    df.loc[:, 'Recoded_duration'] = df['duration'].apply(
        lambda x: 'Singles' if 'min' in str(x) else 'Series'
    )
    
    # Create the Recoded_release_year column based on decades
    def recode_release_year(year):
        if 1920 <= year <= 1929:
            return 'Silent_Era'
        elif 1930 <= year <= 1939:
            return 'Golden_Age'
        elif 1940 <= year <= 1949:
            return 'WW II_Post_War'
        elif 1950 <= year <= 1959:
            return 'Television_Rise'
        elif 1960 <= year <= 1969:
            return 'New_Wave_Movements'
        elif 1970 <= year <= 1979:
            return 'Blockbuster_Era'
        elif 1980 <= year <= 1989:
            return 'Home_Video'
        elif 1990 <= year <= 1999:
            return 'CGI_Rise'
        elif 2000 <= year <= 2009:
            return 'Digital_Revolution'
        elif 2010 <= year <= 2019:
            return 'Streaming_Diversity'
        elif year >= 2020:
            return 'COVID-19_Impact'
        else:
            return 'Unknown'

    df.loc[:, 'Recoded_release_year'] = df['release_year'].apply(recode_release_year)

    # Save the cleaned data to a new CSV file
    df.to_csv('netflix_show_movies.csv', index=False)
    
    return df