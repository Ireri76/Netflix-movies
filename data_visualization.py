# 5. data_visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df):
    plt.figure(figsize=(12, 6))

    # Graph 1: 'Recoded_release_year' and 'type'
    plt.subplot(1, 3, 1)
    sns.countplot(data=df, x='Recoded_release_year', hue='type')
    plt.title('Figure 1: Distribution of Types by Release Year')
    plt.xticks(rotation=90)  # Rotate labels

    # Graph 2: 'type' and 'rating'
    plt.subplot(1, 3, 2)
    sns.countplot(data=df, x='type', hue='rating')
    plt.title('Figure 2: Distribution of Ratings by Type')
    plt.xticks(rotation=90)  # Rotate labels

    # Graph 3: 'type' and 'Recoded_duration'
    plt.subplot(1, 3, 3)
    sns.countplot(data=df, x='type', hue='Recoded_duration')
    plt.title('Figure 3: Distribution of Duration by Type')
    plt.xticks(rotation=90)  # Rotate labels

    plt.tight_layout()
    plt.show()