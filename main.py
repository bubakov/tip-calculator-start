#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Greetings
print("Wlcome to the tip calculator")

# Total bill
total = input("What was the total bill? $")
total = float(total)

# tip in percent
tip = input("What percentage tip would zou like to give? 10, 12, or 15? ")
tip = int(tip)
tip = tip / 100 + 1

# Fill number of people
number_of_people = input("How many people to split the bill? ")
number_of_people = int(number_of_people)

# Calculation
payment = (total / number_of_people) * tip

# rounding exactly on two places, round doesn't show last zero
payment = round(payment, 2)
payment = "{:.2f}".format(payment)

# f-string with round on two places
print(f"Each person should pay: ${payment}")
