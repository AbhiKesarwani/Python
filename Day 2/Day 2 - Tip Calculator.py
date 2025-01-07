print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
no_of_persons = int(input("How many people to split the bill? "))
tip_percent = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
each_pay = (total_bill + total_bill*(tip_percent/100))/no_of_persons  #calculating each person pay
round_2decimal = "{:.2f}".format(each_pay)  #rounding each person pay to 2 decimal places 
print(f"Each person should pay: ${round_2decimal}")


'''Ma'am code

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much percentage of tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")
'''