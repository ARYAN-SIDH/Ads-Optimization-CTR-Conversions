from imports import *

def plot_ctr(df_original):
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Gender', y='CTR', data=df_original, inner='quartile')
    sns.swarmplot(x='Gender', y='CTR', data=df_original, color='k', alpha=0.3)
    plt.title('CTR by Gender')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Location', y='CTR', data=df_original, inner='quartile')
    sns.swarmplot(x='Location', y='CTR', data=df_original, color='k', alpha=0.3)
    plt.title('CTR by Location')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Ad Type', y='CTR', data=df_original, inner='quartile')
    sns.swarmplot(x='Ad Type', y='CTR', data=df_original, color='k', alpha=0.3)
    plt.title('CTR by Ad Type')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Ad Placement', y='CTR', data=df_original, inner='quartile')
    sns.swarmplot(x='Ad Placement', y='CTR', data=df_original, color='k', alpha=0.3)
    plt.title('CTR by Ad Placement')
    plt.show()