from imports import *

def treatment_and_matching(df, df_original):
    df['Treatment'] = (df_original['Clicks'] > 0).astype(int)
    covariates = [col for col in df.columns if col not in ['Click Time', 'Clicks', 'Conversion Rate', 'CTR', 'Treatment', 'Propensity_Score']]

    logit = LogisticRegression(solver='liblinear')
    df['Propensity_Score'] = logit.fit(df[covariates], df['Treatment']).predict_proba(df[covariates])[:, 1]

    treated = df[df['Treatment'] == 1]
    control = df[df['Treatment'] == 0]

    nn = NearestNeighbors(n_neighbors=1, metric='euclidean')
    nn.fit(control[['Propensity_Score']])
    distances, indices = nn.kneighbors(treated[['Propensity_Score']])

    matched_controls = control.iloc[indices.flatten()]
    matched_data = pd.concat([treated, matched_controls])
    return matched_data

