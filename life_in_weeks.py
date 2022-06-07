import time
print("If you live until 90 years old, How many Years, Months, Weeks and Days left ?")
time.sleep(1)

age = int(input("What is your current age ? \n"))

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
time.sleep(1)
message = f'''You have {years_remaining} Years,
{months_remaining} Months,
{weeks_remaining} Weeks,
and {days_remaining} Days lefts...'''

print(message)