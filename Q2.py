# Code to input Gross Income and number of dependents
gross_income = int(input("Enter the taxpayer's Gross Income: "))
numbers_of_dependents = int(input("Enter number of dependents: "))

# Code to calculate and print Tax
standard_deduction = 10000
dependent_deduction = 3000
taxable_income = gross_income - standard_deduction - (dependent_deduction * numbers_of_dependents)
tax = taxable_income * 0.2
print(tax)
