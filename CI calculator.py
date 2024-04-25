def calculate_compound_interest(principal, rate_of_interest, years, compounding_frequency):
    rate = rate_of_interest / 100
    
    amount = principal * (1 + rate / compounding_frequency) ** (compounding_frequency * years)
    compound_interest = amount - principal
    
    return compound_interest

principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the annual interest rate (%): "))
years = int(input("Enter the number of years: "))
compounding_frequency = int(input("Enter how many times a year the interest is compounded: "))

result = calculate_compound_interest(principal, rate_of_interest, years, compounding_frequency)
total_amount = result + principal

print(f"\nThe compound interest after {years} years is: {result:.2f}")
print(f"\nThe total amount after {years} years is: {total_amount:.2f}") 
 