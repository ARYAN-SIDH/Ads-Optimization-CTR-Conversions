from imports import *

def calculate_ate(matched_data):
    ate = matched_data[matched_data['Treatment'] == 1]['Conversion Rate'].mean() - matched_data[matched_data['Treatment'] == 0]['Conversion Rate'].mean()
    print("Estimated Average Treatment Effect (ATE):", round(ate, 6))

