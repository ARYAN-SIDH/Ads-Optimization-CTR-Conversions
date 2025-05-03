from imports import *

def plot_hte(matched_data):
    # Violin Plot: HTE by Gender
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Gender', y='HTE_Estimate', data=matched_data)
    sns.swarmplot(x='Gender', y='HTE_Estimate', data=matched_data, color='k', alpha=0.3, size=2)
    plt.title('HTE by Gender')
    plt.xlabel('Gender')
    plt.ylabel('HTE Estimate')
    plt.show()

    # KDE Plot: HTE by Ad Type (Video vs Others)
    plt.figure(figsize=(10, 6))
    sns.kdeplot(matched_data[matched_data['Ad Type_Video'] == 1]['HTE_Estimate'], label='Video Ads', fill=True)
    sns.kdeplot(matched_data[matched_data['Ad Type_Video'] == 0]['HTE_Estimate'], label='Other Ads', fill=True)
    plt.title('HTE Distribution: Video Ads vs Other Ads')
    plt.xlabel('HTE Estimate')
    plt.legend()
    plt.show()

    # KDE Plot: HTE by Ad Placement (Social Media vs Others)
    plt.figure(figsize=(10, 6))
    sns.kdeplot(matched_data[matched_data['Ad Placement_Social Media'] == 1]['HTE_Estimate'], label='Social Media Ads', fill=True)
    sns.kdeplot(matched_data[matched_data['Ad Placement_Social Media'] == 0]['HTE_Estimate'], label='Other Placements', fill=True)
    plt.title('HTE Distribution: Social Media Ads vs Other Placements')
    plt.xlabel('HTE Estimate')
    plt.legend()
    plt.show()

    # Scatter Plot: HTE vs Income
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Income', y='HTE_Estimate', data=matched_data)
    plt.title('HTE vs Income')
    plt.xlabel('Income')
    plt.ylabel('HTE Estimate')
    plt.show()

    # Scatter Plot: HTE vs Age
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='HTE_Estimate', data=matched_data)
    plt.title('HTE vs Age')
    plt.xlabel('Age')
    plt.ylabel('HTE Estimate')
    plt.show()