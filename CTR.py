from imports import pd, plt, sns, LabelEncoder, StandardScaler
from data_preprocessing import df_demo
import warnings

# Suppress specific UserWarnings from seaborn
warnings.filterwarnings("ignore", category=UserWarning, module="seaborn.categorical")

def ctr_gender(df):
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Gender', y='CTR', data=df, inner='quartile')
    sns.swarmplot(x='Gender', y='CTR', data=df, color='k', alpha=0.3)
    plt.title('CTR by Gender')
    plt.show()

ctr_gender(df_demo)

def ctr_location(df):
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Location_Urban', y='CTR', data=df, inner='quartile')
    sns.swarmplot(x='Location_Urban', y='CTR', data=df, color='k', alpha=0.3)
    plt.title('CTR by Location (Urban vs Others)')
    plt.show()

ctr_location(df_demo)

def ctr_adtype(df):
    plt.figure(figsize=(8, 6))
    sns.stripplot(x='Ad Type_Video', y='CTR', data=df, jitter=True, alpha=0.4)
    plt.title("CTR by Ad Type (Video vs Others)")
    plt.show()

ctr_adtype(df_demo)

def ctr_adplacement(df):
    plt.figure(figsize=(8, 6))
    sns.stripplot(x='Ad Placement_Website', y='CTR', data=df, jitter=True, alpha=0.4)
    plt.title("CTR by Ad Placement (Website vs Others)")
    plt.show()

ctr_adplacement(df_demo)

