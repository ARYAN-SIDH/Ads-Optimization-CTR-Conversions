from imports import *

def estimate_hte(matched_data, covariates):
    X = matched_data[covariates]
    Y = matched_data['Conversion Rate']
    T = matched_data['Treatment']

    estimator = CausalForestDML(
        model_t=RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42),
        model_y=RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42),
        discrete_treatment=True,
        cv=3,
        random_state=42
    )

    estimator.fit(Y, T, X=X)
    matched_data['HTE_Estimate'] = estimator.effect(X)
    return matched_data
