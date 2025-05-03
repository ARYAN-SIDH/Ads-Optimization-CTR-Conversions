# Conversions.py
from imports import pd, plt, sns, LabelEncoder, StandardScaler
from data_preprocessing import df_demo

def distribution_plots(df_original):
    # Create subplots for numerical feature distributions
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Histogram for CTR
    sns.histplot(df_original['CTR'], bins=30, kde=True, ax=axes[0, 0])
    axes[0, 0].set_title("Distribution of CTR")

    # Histogram for Conversion Rate
    sns.histplot(df_original['Conversion Rate'], bins=30, kde=True, ax=axes[0, 1])
    axes[0, 1].set_title("Distribution of Conversion Rate")

    # Histogram for Clicks
    sns.histplot(df_original['Clicks'], bins=30, kde=True, ax=axes[1, 0])
    axes[1, 0].set_title("Distribution of Clicks")
    axes[1, 0].set_xlim(0, None)  # Ensure x-axis starts from 0

    # Histogram for Income
    sns.histplot(df_original['Income'], bins=30, kde=True, ax=axes[1, 1])
    axes[1, 1].set_title("Distribution of Income")

    # Adjust layout
    plt.tight_layout()
    plt.show()

distribution_plots(df_demo)



