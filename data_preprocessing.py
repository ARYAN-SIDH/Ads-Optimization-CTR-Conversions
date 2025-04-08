from imports import pd, LabelEncoder, StandardScaler

df_demo = pd.read_csv("Demographic.csv")

# Convert Click Time to datetime format
df_demo['Click Time'] = pd.to_datetime(df_demo['Click Time'])
# Encode Gender (Binary: Male/Female/Other) using Label Encoding
label_encoder = LabelEncoder()
df_demo['Gender'] = label_encoder.fit_transform(df_demo['Gender'])

# One-Hot Encoding for categorical variables
categorical_columns = ['Location', 'Ad Type', 'Ad Topic', 'Ad Placement']
df_demo = pd.get_dummies(df_demo, columns=categorical_columns, drop_first=True)

# Standardize numerical features
scaler = StandardScaler()
numerical_columns = ['Age', 'Income', 'Clicks', 'CTR', 'Conversion Rate']
df_demo[numerical_columns] = scaler.fit_transform(df_demo[numerical_columns])
df_demo['Clicks'] = df_demo['Clicks'].apply(lambda x: max(x, 0))

# Apply standardization
scaler = StandardScaler()
numerical_columns = ['Age', 'Income', 'Clicks', 'CTR', 'Conversion Rate']
df_demo[numerical_columns] = scaler.fit_transform(df_demo[numerical_columns])