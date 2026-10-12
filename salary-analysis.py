
# Employee Salary Analysis

# Employee salary data
salaries = [25000, 32000, 28000, 45000, 38000, 30000, 50000, 27000]

# Calculate salary statistics
total_salary = sum(salaries)
average_salary = total_salary / len(salaries)
highest_salary = max(salaries)
lowest_salary = min(salaries)

# Display results
print("=" * 40)
print("       EMPLOYEE SALARY ANALYSIS")
print("=" * 40)

print(f"Number of Employees : {len(salaries)}")
print(f"Total Salary        : Rs. {total_salary:,.2f}")
print(f"Average Salary      : Rs. {average_salary:,.2f}")
print(f"Highest Salary      : Rs. {highest_salary:,.2f}")
print(f"Lowest Salary       : Rs. {lowest_salary:,.2f}")

print("=" * 40)

# Compare salaries with the calculated average
print("\nSalary Comparison:")

for index, salary in enumerate(salaries, start=1):
    status = "Above average" if salary > average_salary else (
        "Below average" if salary < average_salary else "Equal to average"
    )
    print(f"Employee {index}: Rs. {salary:,.2f} - {status}")
