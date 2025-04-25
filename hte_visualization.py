from imports import *

def plot_hte(matched_data):
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Gender', y='HTE_Estimate', data=matched_data)
    plt.title('HTE by Gender')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.kdeplot(matched_data[matched_data['Ad Type_Video'] == 1]['HTE_Estimate'], label='Video Ads', fill=True)
    sns.kdeplot(matched_data[matched_data['Ad Type_Video'] == 0]['HTE_Estimate'], label='Other Ads', fill=True)
    plt.title('HTE Distribution: Video Ads vs Other Ads')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.kdeplot(matched_data[matched_data['Ad Placement_Social Media'] == 1]['HTE_Estimate'], label='Social Media Ads', fill=True)
    sns.kdeplot(matched_data[matched_data['Ad Placement_Social Media'] == 0]['HTE_Estimate'], label='Other Placements', fill=True)
    plt.title('HTE Distribution: Social Media Ads vs Other Placements')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Income', y='HTE_Estimate', data=matched_data)
    plt.title('HTE vs Income')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='HTE_Estimate', data=matched_data)
    plt.title('HTE vs Age')
    plt.show()
