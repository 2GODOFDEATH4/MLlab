# Step 1: Observed data (contingency table)
observed = [[20, 15],  # Row 1
            [30, 35]]  # Row 2

# Step 2: Calculate row totals, column totals, and grand total
row_totals = [sum(row) for row in observed]
col_totals = [sum(col) for col in zip(*observed)]
grand_total = sum(row_totals)

# Step 3: Calculate expected frequencies
expected = [[(row_totals[i] * col_totals[j]) / grand_total for j in range(len(col_totals))] for i in range(len(row_totals))]

# Step 4: Calculate Chi-square statistic
chi_square_stat = 0
for i in range(len(observed)):
    for j in range(len(observed[i])):
        o = observed[i][j]  # Observed frequency
        e = expected[i][j]  # Expected frequency
        chi_square_stat += ((o - e) ** 2) / e

# Step 5: Degrees of freedom (df = (number of rows - 1) * (number of columns - 1))
df = (len(observed) - 1) * (len(observed[0]) - 1)

# Step 6: Critical value (Look up from Chi-square table for df and alpha level)
alpha = 0.05
# For df = 1 and alpha = 0.05, the critical value is approximately 3.841

critical_value = 3.841  # From Chi-square table for df = 1 and alpha = 0.05

# Step 7: Compare Chi-square statistic with critical value
print(f'Chi-square statistic: {chi_square_stat}')
print(f'Critical value: {critical_value}')

# Step 8: Conclusion
if chi_square_stat > critical_value:
    print("Reject the null hypothesis: The variables are not independent (there is a relationship).")
else:
    print("Fail to reject the null hypothesis: The variables are independent (no significant relationship).")