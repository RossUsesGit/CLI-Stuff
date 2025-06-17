# Ask the user for their birthyear and compute their age in days.
# This is a simpler version and does not account for when the birthday is, what day it is today, etc. 
# It only counts on the birthyear.

from datetime import datetime

current_year = datetime.now().year
your_birthyear = int(input("Please enter your birthyear: "))

your_age_in_years = current_year - your_birthyear

your_age_in_days = your_age_in_years * 365

print("Theoretically, you are",your_age_in_days,"days old!")