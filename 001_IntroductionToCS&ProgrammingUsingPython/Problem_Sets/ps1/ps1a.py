"""
@author: Anirudh Sharma

You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and
decide that you want to start saving to buy a house.  As housing prices are very high in the
Bay Area, you realize you are going to have to save for several years before you can afford
to make the down payment on a house. In Part A, we are going to determine how long it will take
you to save enough money to make the down payment given the following assumptions:
1. Call the cost of your dream home TOTAL_COST.
2. Call the portion of the cost needed for a down payment PORTION_DOWN_PAYMENT. For
simplicity, assume that PORTION_DOWN_PAYMENT = 0.25 (25%).
3. Call the amount that you have saved thus far CURRENT_SAVINGS. You start with a current
savings of $0.
4. Assume that you invest your current savings wisely, with an annual return of r (in other words,
at the end of each month, you receive an additional CURRENT_SAVINGS*r/12 funds to put into
your savings – the 12 is because r is an annual rate). Assume that your investments earn a
return of r = 0.04 (4%).
5. Assume your annual salary is ANNUAL_SALARY.
6. Assume you are going to dedicate a certain amount of your salary each month to saving for
the down payment. Call that PORTION_SAVED. This variable should be in decimal form (i.e. 0.1
for 10%).
7. At the end of each month, your savings will be increased by the return on your investment,
plus a percentage of your monthly salary (annual salary / 12).
Write a program to calculate how many months it will take you to save up enough money for a down
payment. You will want your main variables to be floats, so you should cast user inputs to floats .1
Your program should ask the user to enter the following variables:
1. The starting annual salary (ANNUAL_SALARY)
2. The portion of salary to be saved (PORTION_SAVED)
3. The cost of your dream home (TOTAL_COST)
"""


# Starting annual salary
ANNUAL_SALARY = float(input("Enter your annual salary: "))
# The portion of the salary to be saved
PORTION_SAVED = float(input("Enter the percent of your salary to save, as a decimal: "))
# Cost of the dream home
TOTAL_COST = float(input("Enter the cost of your dream home: "))

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
    CURRENT_SAVINGS += CURRENT_SAVINGS * R / 12 + MONTHLY_SALARY
    COUNTER += 1


print("Number of months: " + str(COUNTER))
