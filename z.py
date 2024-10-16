import math
from scipy import stats

# Step 1: Sample data
sample = [2.5, 3.6, 2.8, 3.2, 2.9]
population_mean = 3.0  # Hypothesized population mean
population_std = 0.5  # Known population standard deviation

# Step 2: Calculate sample mean
sample_mean = sum(sample) / len(sample)

# Step 3: Calculate sample size
n = len(sample)

# Step 4: Calculate standard error (SE) using population standard deviation
se = population_std / math.sqrt(n)

# Step 5: Calculate z-statistic
z_stat = (sample_mean - population_mean) / se

# Step 6: Find the critical z-value for a one-tailed test with alpha 0.05
alpha = 0.05
z_critical = stats.norm.ppf(1 - alpha)  # For right-tailed test

# Step 7: Compare z-statistic with critical z-value
print(f'Sample mean: {sample_mean}')
print(f'Z-statistic: {z_stat}')
print(f'Critical z-value: {z_critical}')

# Step 8: Conclusion for a right-tailed test
if z_stat > z_critical:
    print("Reject the null hypothesis: The sample mean is significantly greater than the population mean.")
else:
    print("Fail to reject the null hypothesis: The sample mean is not significantly greater than the population mean.")