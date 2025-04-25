from imports import *

def plot_conversion(df_original):
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Gender', y='Conversion Rate', data=df_original, inner='quartile')
    sns.swarmplot(x='Gender', y='Conversion Rate', data=df_original, color='k', alpha=0.3)
    plt.title('Conversion Rate by Gender')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Location', y='Conversion Rate', data=df_original, inner='quartile')
    sns.swarmplot(x='Location', y='Conversion Rate', data=df_original, color='k', alpha=0.3)
    plt.title('Conversion Rate by Location')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Ad Type', y='Conversion Rate', data=df_original, inner='quartile')
    sns.swarmplot(x='Ad Type', y='Conversion Rate', data=df_original, color='k', alpha=0.3)
    plt.title('Conversion Rate by Ad Type')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Ad Placement', y='Conversion Rate', data=df_original, inner='quartile')
    sns.swarmplot(x='Ad Placement', y='Conversion Rate', data=df_original, color='k', alpha=0.3)
    plt.title('Conversion Rate by Ad Placement')
    plt.show()
