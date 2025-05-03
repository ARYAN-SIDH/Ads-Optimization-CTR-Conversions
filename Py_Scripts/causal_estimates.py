# 📂 causal_estimates.py
from imports import *

def calculate_ate(matched_data):
    treated_mean = matched_data[matched_data['Treatment'] == 1]['Conversion Rate'].mean()
    control_mean = matched_data[matched_data['Treatment'] == 0]['Conversion Rate'].mean()
    ate = treated_mean - control_mean
    print("Estimated Average Treatment Effect (ATE):", round(ate, 6))

def estimate_hte(matched_data, covariates):
    Y = matched_data['Conversion Rate']
    T = matched_data['Treatment']
    X = matched_data[covariates]

    estimator = CausalForestDML(
        model_t=RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42),
        model_y=RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42),
        discrete_treatment=True,
        cv=3,
        random_state=42
    )

    estimator.fit(Y, T, X=X)
    hte_predictions = estimator.effect(X)
    matched_data['HTE_Estimate'] = hte_predictions

    # Print a sample and summary
    print(matched_data[['Age', 'Gender', 'Income', 'HTE_Estimate']].head())
    print("\nSummary of HTE Estimates:\n", matched_data['HTE_Estimate'].describe())

    return matched_data
