from imports import *


def plot_eda(df_original):
    distribution_features = ['CTR', 'Conversion Rate', 'Clicks', 'Income']
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    for idx, feature in enumerate(distribution_features):
        sns.histplot(df_original[feature], bins=30, kde=True, ax=axes[idx // 2, idx % 2])
        axes[idx // 2, idx % 2].set_title(f"Distribution of {feature}")
        if feature == 'Clicks':
            axes[idx // 2, idx % 2].set_xlim(0, None)

    plt.tight_layout()
    plt.show()