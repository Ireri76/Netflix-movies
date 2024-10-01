# 6. data_analysis.py
import pandas as pd
from scipy.stats import chi2_contingency

def chi_square_test(df, column1, column2):
    cross_tab = pd.crosstab(df[column1], df[column2])
    chi2, p, dof, expected = chi2_contingency(cross_tab)
    
    print(f"Chi-Square Test between {column1} and {column2}")
    print(f"Chi2 Statistic: {chi2}, p-value: {p}\n")
