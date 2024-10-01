# 7.main.py
from data_preparation import load_data
from data_cleaning import clean_data
from data_evaluation import evaluate_data
from data_exploration import explore_data
from data_visualization import visualize_data
from data_analysis import chi_square_test

if __name__ == "__main__":
    # Step 1: Load original Netflix data
    df = load_data('netflix_data.csv') 
    
    # Step 2: Clean data and save it as 'netflix_show_movies.csv'
    df = clean_data(df)  
    
    # Step 3: Load the cleaned data for further evaluation
    df_cleaned = evaluate_data('netflix_show_movies.csv')
    
    # Step 4: Explore Data
    explore_data(df_cleaned)
    
    # Step 5: Visualize Data
    visualize_data(df_cleaned)
    
    # Step 6: Run Chi-square tests without additional info display
    chi_square_test(df_cleaned, 'type', 'Recoded_release_year')
    chi_square_test(df_cleaned, 'type', 'rating')
    chi_square_test(df_cleaned, 'type', 'Recoded_duration')