import math
from scipy import stats  # For critical t-value

# Step 1: Sample data
sample = [2.5, 3.6, 2.8, 3.2, 2.9]
population_mean = 3.0  # Hypothesized population mean

# Step 2: Calculate sample mean
sample_mean = sum(sample) / len(sample)

# Step 3: Calculate sample variance and standard deviation
variance = sum((x - sample_mean) ** 2 for x in sample) / (len(sample) - 1)
std_dev = math.sqrt(variance)

# Step 4: Calculate standard error (SE)
n = len(sample)
se = std_dev / math.sqrt(n)

# Step 5: Calculate t-statistic
t_stat = (sample_mean - population_mean) / se

# Step 6: Degrees of freedom
df = n - 1

# Step 7: Critical t-value for alpha 0.05 (two-tailed test)
alpha = 0.05
t_critical = stats.t.ppf(1 - alpha / 2, df)

# Step 8: Compare t-statistic with critical t-value
print(f'Sample mean: {sample_mean}')
print(f'T-statistic: {t_stat}')
print(f'Degrees of freedom: {df}')
print(f'Critical t-value: {t_critical}')

# Step 9: Conclusion
if abs(t_stat) > t_critical:
    print("Reject the null hypothesis: The sample mean is significantly different from the population mean.")
else:
    print("Fail to reject the null hypothesis: No significant difference between the sample mean and population mean.")