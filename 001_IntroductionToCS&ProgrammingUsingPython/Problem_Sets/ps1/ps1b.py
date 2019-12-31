"""
@author: Anirudh Sharma

In Part A, we unrealistically assumed that your salary didn’t change. But you are an MIT graduate,
and clearly you are going to be worth more to your company over time! So we are going to build on
your solution to Part A by factoring in a raise every six months.
In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify
your program to include the following
1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
2. After the 6th month, increase your salary by that percentage.  Do the same after the 12th
month, the 18  month, and so on.
Write a program to calculate how many months it will take you save up enough money for a down
payment.  LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the
required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
1. The starting annual salary (annual_salary)
2
2. The percentage of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
4. The semi­annual salary raise (semi_annual_raise)

"""

# Starting annual salary
ANNUAL_SALARY = float(input("Enter your annual salary: "))
# The portion of the salary to be saved
PORTION_SAVED = float(input("Enter the percent of your salary to save, as a decimal: "))
# Cost of the dream home
TOTAL_COST = float(input("Enter the cost of your dream home: "))
# Semi annual raise in the salary
SEMI_ANNUAL_RAISE = float(input("Enter the semi­annual raise, as a decimal: "))

#Down payment - 25% of the total cost
PORTION_DOWN_PAYMENT = 0.25 * TOTAL_COST
# Current saving
CURRENT_SAVINGS = 0
# Investment return - 4%
R = 0.04

# Monthly salary
MONTHLY_SALARY = ANNUAL_SALARY * PORTION_SAVED / 12
# At the end of first month
CURRENT_SAVINGS = MONTHLY_SALARY
# Month COUNTER
COUNTER = 1
# Loop until we reach a value greater than or equal to the down payment
while PORTION_DOWN_PAYMENT >= CURRENT_SAVINGS:
    if COUNTER % 6 == 0:
        MONTHLY_SALARY = MONTHLY_SALARY * (1 + SEMI_ANNUAL_RAISE)
    CURRENT_SAVINGS += CURRENT_SAVINGS * R / 12 + MONTHLY_SALARY
    COUNTER += 1

print("Number of months: " + str(COUNTER))
