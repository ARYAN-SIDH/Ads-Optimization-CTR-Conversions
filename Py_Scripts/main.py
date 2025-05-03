# 📂 main.py

from imports import *
from data_preprocessing import load_and_preprocess
from ctr_analysis import plot_ctr_analysis
from conversion_analysis import plot_conversion_analysis
from treatment_matching import treatment_and_matching
from causal_estimates import calculate_ate
from causal_estimates import estimate_hte
from hte_visualization import plot_hte
from campaign_analysis import analyze_campaign_performance, radar_chart_campaign_comparison

def main():
    # Load and preprocess user-level ad data
    df_demo, df_original = load_and_preprocess("Demographic.csv")

    # CTR and Conversion Analysis
    plot_ctr_analysis(df_original, df_demo)
    plot_conversion_analysis(df_original, df_demo)

    # Causal Inference: Treatment definition and Propensity Score Matching
    matched_data = treatment_and_matching(df_demo, df_original)

    # ATE Calculation
    calculate_ate(matched_data)

    # HTE Estimation and Visualization
    covariates = [col for col in matched_data.columns if col not in [
        'Click Time', 'Clicks', 'Conversion Rate', 'CTR', 'Treatment', 'Propensity_Score', 'HTE_Estimate'
    ]]
    matched_data = estimate_hte(matched_data, covariates)
    plot_hte(matched_data)

    # Load and Analyze Campaign Dataset
    df_campaign = pd.read_csv("marketing_campaign_dataset.csv")
    analyze_campaign_performance(df_campaign)
    radar_chart_campaign_comparison(df_campaign)


if __name__ == "__main__":
    main()
