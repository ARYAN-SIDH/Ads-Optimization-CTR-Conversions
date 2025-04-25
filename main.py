from data_preprocessing import load_and_preprocess
from eda_plots import plot_eda
from treatment_matching import treatment_and_matching
from ate_calculation import calculate_ate
from hte_estimation import estimate_hte
from hte_visualization import plot_hte


# Execute Project
if __name__ == "__main__":
    df_demo, df_original = load_and_preprocess('Demographic.csv')
    plot_eda(df_original)

    matched_data = treatment_and_matching(df_demo, df_original)
    calculate_ate(matched_data)

    covariates = [col for col in matched_data.columns if col not in ['Click Time', 'Clicks', 'Conversion Rate', 'CTR', 'Treatment', 'Propensity_Score', 'HTE_Estimate']]
    matched_data = estimate_hte(matched_data, covariates)
    plot_hte(matched_data)