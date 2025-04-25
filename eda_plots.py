from imports import *

def plot_eda(df_original):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    sns.histplot(df_original['CTR'], bins=30, kde=True, ax=axes[0, 0])
    axes[0, 0].set_title("Distribution of CTR")
    sns.histplot(df_original['Conversion Rate'], bins=30, kde=True, ax=axes[0, 1])
    axes[0, 1].set_title("Distribution of Conversion Rate")
    sns.histplot(df_original['Clicks'], bins=30, kde=True, ax=axes[1, 0])
    axes[1, 0].set_title("Distribution of Clicks")
    axes[1, 0].set_xlim(0, None)
    sns.histplot(df_original['Income'], bins=30, kde=True, ax=axes[1, 1])
    axes[1, 1].set_title("Distribution of Income")
    plt.tight_layout()
    plt.show()
