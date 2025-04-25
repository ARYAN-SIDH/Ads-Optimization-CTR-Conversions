from imports import *

def load_and_preprocess(file_path):
    df = pd.read_csv(file_path)
    df_original = df.copy()
    label_encoder = LabelEncoder()
    df['Gender'] = label_encoder.fit_transform(df['Gender'])

    categorical_columns = ['Location', 'Ad Type', 'Ad Topic', 'Ad Placement']
    df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

    scaler = StandardScaler()
    numerical_columns = ['Age', 'Income', 'Clicks', 'CTR', 'Conversion Rate']
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    return df, df_original
