# 📂 campaign_analysis.py
from imports import *

def analyze_campaign_performance(df_campaign):
    # Step 1: Group by Campaign Type and summarize
    metrics = ['ROI', 'Conversion_Rate', 'Engagement_Score']
    campaign_summary = df_campaign.groupby("Campaign_Type")[metrics].mean().reset_index()

    # Step 2: Bar Plots
    plt.figure(figsize=(16, 5))

    plt.subplot(1, 3, 1)
    sns.barplot(x="ROI", y="Campaign_Type", data=campaign_summary, palette="Blues_d")
    plt.title("Average ROI by Campaign Type")

    plt.subplot(1, 3, 2)
    sns.barplot(x="Conversion_Rate", y="Campaign_Type", data=campaign_summary, palette="Greens_d")
    plt.title("Avg Conversion Rate by Campaign Type")

    plt.subplot(1, 3, 3)
    sns.barplot(x="Engagement_Score", y="Campaign_Type", data=campaign_summary, palette="Purples_d")
    plt.title("Avg Engagement Score by Campaign Type")

    plt.tight_layout()
    plt.show()


def radar_chart_campaign_comparison(df_campaign):
    # Step 1: Group and normalize
    metrics = ['ROI', 'Conversion_Rate', 'Engagement_Score']
    summary_df = df_campaign.groupby('Campaign_Type')[metrics].mean()
    normalized_df = (summary_df - summary_df.min()) / (summary_df.max() - summary_df.min())

    # Step 2: Radar chart setup
    categories = list(normalized_df.columns)
    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    # Step 3: Plot radar chart
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    for campaign in normalized_df.index:
        values = normalized_df.loc[campaign].tolist()
        values += values[:1]
        ax.plot(angles, values, label=campaign)
        ax.fill(angles, values, alpha=0.1)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)
    plt.title("Radar Chart: Campaign Type Performance Comparison", size=14)
    plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1.05))
    plt.tight_layout()
    plt.show()
