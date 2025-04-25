from imports import *

def analyze_campaign_data(file_path):
    df = pd.read_csv(file_path)

    # Convert dollar strings to float
    df['Acquisition_Cost'] = df['Acquisition_Cost'].replace('[\$,]', '', regex=True).astype(float)

    # Group by Campaign Type and calculate means
    campaign_summary = df.groupby('Campaign_Type')[['ROI', 'Conversion_Rate', 'Engagement_Score']].mean().reset_index()

    # Plot bar charts
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    sns.barplot(x='ROI', y='Campaign_Type', data=campaign_summary, ax=axes[0], palette="Blues_d")
    axes[0].set_title("Average ROI by Campaign Type")

    sns.barplot(x='Conversion_Rate', y='Campaign_Type', data=campaign_summary, ax=axes[1], palette="Greens_d")
    axes[1].set_title("Avg Conversion Rate by Campaign Type")

    sns.barplot(x='Engagement_Score', y='Campaign_Type', data=campaign_summary, ax=axes[2], palette="Purples_d")
    axes[2].set_title("Avg Engagement Score by Campaign Type")

    plt.tight_layout()
    plt.show()

    return campaign_summary
