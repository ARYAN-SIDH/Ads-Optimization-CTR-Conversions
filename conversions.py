import warnings
from imports import pd, plt, sns, LabelEncoder, StandardScaler
from data_preprocessing import df_demo
# Suppress specific UserWarnings from seaborn
warnings.filterwarnings("ignore", category=UserWarning, module="seaborn.categorical")

# Plot 1: Conversion Rate by Gender
def conversion_gender():
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Gender', y='Conversion Rate', data=df_demo, inner='quartile')
    sns.swarmplot(x='Gender', y='Conversion Rate', data=df_demo, color='k', alpha=0.3)
    plt.title("Conversion Rate by Gender")
    plt.show()

# Plot 2: Conversion Rate by Location
plt.figure(figsize=(8, 6))
sns.violinplot(x='Location_Urban', y='Conversion Rate', data=df_demo, inner='quartile')
sns.swarmplot(x='Location_Urban', y='Conversion Rate', data=df_demo, color='k', alpha=0.3)
plt.title("Conversion Rate by Location (Urban vs Others)")
plt.show()

# Plot 3: Conversion Rate by Ad Type (Video)
plt.figure(figsize=(8, 6))
sns.violinplot(x='Ad Type_Video', y='Conversion Rate', data=df_demo, inner='quartile')
sns.swarmplot(x='Ad Type_Video', y='Conversion Rate', data=df_demo, color='k', alpha=0.3)
plt.title("Conversion Rate by Ad Type (Video vs Others)")
plt.show()

# Plot 4: Conversion Rate by Ad Placement (Social Media)
plt.figure(figsize=(8, 6))
sns.violinplot(x='Ad Placement_Social Media', y='Conversion Rate', data=df_demo, inner='quartile')
sns.swarmplot(x='Ad Placement_Social Media', y='Conversion Rate', data=df_demo, color='k', alpha=0.3)
plt.title("Conversion Rate by Ad Placement (Social Media vs Others)")
plt.show()

# Plot 5: Conversion Rate by Ad Placement (Website)
plt.figure(figsize=(8, 6))
sns.violinplot(x='Ad Placement_Website', y='Conversion Rate', data=df_demo, inner='quartile')
sns.swarmplot(x='Ad Placement_Website', y='Conversion Rate', data=df_demo, color='k', alpha=0.3)
plt.title("Conversion Rate by Ad Placement (Website vs Others)")
plt.show()
