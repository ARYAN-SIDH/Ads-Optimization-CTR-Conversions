# 📂 conversion_analysis.py
from imports import *

def plot_conversion_analysis(df_original, df_demo):
    # Conversion Rate by Gender
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Gender', y='Conversion Rate', data=df_original)
    sns.swarmplot(x='Gender', y='Conversion Rate', data=df_original, color='k', alpha=0.3, size=2)
    plt.title('Conversion Rate by Gender')
    plt.show()

    # Conversion Rate by Social Media Ad Placement
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Ad Placement_Social Media', y='Conversion Rate', data=df_demo)
    sns.swarmplot(x='Ad Placement_Social Media', y='Conversion Rate', data=df_demo, color='k', alpha=0.3, size=2)
    plt.xlabel('Social Media Ad (1=True, 0=Other)')
    plt.title('Conversion Rate by Ad Placement (Social Media vs Others)')
    plt.show()

    # Conversion Rate by Website Ad Placement
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Ad Placement_Website', y='Conversion Rate', data=df_demo)
    sns.swarmplot(x='Ad Placement_Website', y='Conversion Rate', data=df_demo, color='k', alpha=0.3, size=2)
    plt.xlabel('Website Ad (1=True, 0=Other)')
    plt.title('Conversion Rate by Ad Placement (Website vs Others)')
    plt.show()
