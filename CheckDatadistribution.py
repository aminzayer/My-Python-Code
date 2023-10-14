import numpy as np
from scipy import stats

data = [2005, 2194, 2371, 2502, 2278, 2153, 2345, 3302, 3221, 3350, 4054, 4521, 4350, 4047, 4478, 5432, 6099]

# Check if the data is normally distributed using the Shapiro-Wilk test
stat, p = stats.shapiro(data)

if p > 0.05:
    print("The data is already normally distributed.")
else:
    print("The data is not normally distributed. Transforming the data...")

    # Log transformation of the data
    log_transformed_data = np.log(data)

    # Check if the transformed data is normally distributed
    stat, p = stats.shapiro(log_transformed_data)

    if p > 0.05:
        print("After log transformation, the data is now normally distributed.")
        print("Transformed Data:", log_transformed_data)
    else:
        print("Log transformation did not result in a normal distribution. Additional normalization may be needed.")
