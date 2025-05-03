# 📂 ctr_analysis.py
from imports import *

def plot_ctr_analysis(df_original, df_demo):
    # CTR by Gender
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Gender', y='CTR', data=df_original)
    sns.swarmplot(x='Gender', y='CTR', data=df_original, color='k', alpha=0.3, size=2)
    plt.title('CTR by Gender')
    plt.show()

    # CTR by Location
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Location', y='CTR', data=df_original)
    sns.swarmplot(x='Location', y='CTR', data=df_original, color='k', alpha=0.3, size=2)
    plt.title('CTR by Location')
    plt.show()

    # CTR by Ad Type (Video vs Others)
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Ad Type_Video', y='CTR', data=df_demo)
    sns.swarmplot(x='Ad Type_Video', y='CTR', data=df_demo, color='k', alpha=0.3, size=2)
    plt.xlabel('Video Ad (1=True, 0=Other)')
    plt.title('CTR by Ad Type (Video vs Others)')
    plt.show()

    # CTR by Social Media Ad Placement
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Ad Placement_Social Media', y='CTR', data=df_demo)
    sns.swarmplot(x='Ad Placement_Social Media', y='CTR', data=df_demo, color='k', alpha=0.3, size=2)
    plt.xlabel('Social Media Ad (1=True, 0=Other)')
    plt.title('CTR by Ad Placement (Social Media vs Others)')
    plt.show()

    # CTR by Website Ad Placement
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Ad Placement_Website', y='CTR', data=df_demo)
    sns.swarmplot(x='Ad Placement_Website', y='CTR', data=df_demo, color='k', alpha=0.3, size=2)
    plt.xlabel('Website Ad (1=True, 0=Other)')
    plt.title('CTR by Ad Placement (Website vs Others)')
    plt.show()
