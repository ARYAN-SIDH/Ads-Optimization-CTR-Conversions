## Causal Machine Learning for A/B Testing & Ads Optimization

### Introduction

In the digital advertising industry, businesses constantly seek to optimize their ad campaigns to improve engagement and conversion rates. However, traditional statistical methods often fail to capture the true causal effect of an advertisement on user behavior. This project focuses on applying causal machine learning techniques to measure the impact of ads on click-through rates (CTR) and conversions.

### Project Objective

The goal of this project is to accurately estimate the causal effect of online advertisements on user engagement by leveraging advanced statistical and machine learning techniques. Specifically, we aim to:

- Distinguish correlation from causation in ad performance data.

- Estimate the Average Treatment Effect (ATE) – measuring the true lift caused by ads.

- Optimize ad targeting and bidding strategies based on causal insights.

In this project, we aim to develop a causal machine learning framework for optimizing digital ad campaigns by accurately measuring the true causal impact of ads on user engagement (e.g., click-through rate, conversions). Traditional A/B testing methods often fail to account for confounders like user demographics and browsing history, leading to biased estimates. We will leverage Double Machine Learning (DML), Bayesian Causal Inference, and Uplift Modeling to estimate individual treatment effects and identify the most responsive users.

### Datasets Used

We will use two datasets for this project:

- Online Advertisement Click-Through Rates (Mendeley Data): Contains user demographics, ad types, and click behavior, helping to analyze engagement patterns.

- Criteo Conversion Logs Dataset: Tracks user conversions after seeing ads, making it useful for measuring true ad impact.

### Key Techniques & Methods

To ensure robust causal estimation, we will apply the following methods:

- Propensity Score Matching (PSM): Matching treated and control users based on their likelihood of seeing an ad.

- Inverse Probability Weighting (IPW): Adjusting for selection bias.

- Difference-in-Differences (DiD): Comparing pre/post exposure effects.

- Double Machine Learning (DML): Using ML models to control for confounding factors.

- Causal Forests & Uplift Modeling: Predicting heterogeneous treatment effects.

### Expected Outcomes

- Quantified causal impact of ads on CTR and conversions.

- Optimized ad targeting strategies based on user response.

- Actionable insights for budget allocation and personalized ad delivery.

