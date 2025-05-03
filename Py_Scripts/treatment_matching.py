from imports import *

def treatment_and_matching(df_demo, df_original):
    # Define Treatment: 1 if user clicked at least once, else 0
    df_demo['Treatment'] = (df_demo['Clicks'] > 0).astype(int)

    # Propensity Score Estimation
    covariates = [
        'Age', 'Gender', 'Income',
        'Location_Suburban', 'Location_Urban',
        'Ad Type_Native', 'Ad Type_Text', 'Ad Type_Video',
        'Ad Topic_Finance', 'Ad Topic_Food', 'Ad Topic_Health',
        'Ad Topic_Technology', 'Ad Topic_Travel',
        'Ad Placement_Social Media', 'Ad Placement_Website'
    ]
    
    logit = LogisticRegression(solver='liblinear')
    df_demo['Propensity_Score'] = logit.fit(df_demo[covariates], df_demo['Treatment'])\
                                        .predict_proba(df_demo[covariates])[:, 1]

    # Nearest Neighbor Matching
    treated = df_demo[df_demo['Treatment'] == 1]
    control = df_demo[df_demo['Treatment'] == 0]

    nn = NearestNeighbors(n_neighbors=1)
    nn.fit(control[['Propensity_Score']])
    distances, indices = nn.kneighbors(treated[['Propensity_Score']])
    matched_controls = control.iloc[indices.flatten()]

    # Combine treated with matched control group
    matched_data = pd.concat([treated, matched_controls], ignore_index=True)

    return matched_data

