from datetime import datetime, date


now=datetime.today()
print(now)

#age calculator

# dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
# dob = datetime.strptime(dob_input, "%Y-%m-%d").date()  #to convert for cslcukation
# today = date.today()
# print(today)
# age = today.year - dob.year
# if (today.month, today.day) < (dob.month, dob.day):
#     age -= 1
# print(f"Your current age is: {age} years")

#acept two dates

# date1_input=input("enter you first date(YYYY-MM-DD)")
# date2_input=input("enter you second date(YYYY-MM-DD)")
# date1_str=datetime.strptime(date1_input,"%Y-%m-%d").date()
# date2_str=datetime.strptime(date2_input,"%Y-%m-%d").date()

# differnce_date=abs((date1_str-date2_str).days)
# print("difference between",differnce_date)


