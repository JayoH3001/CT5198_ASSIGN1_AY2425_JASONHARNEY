# Jason Harney
# 12461932

#init list called 'customer_numbers that stores the customer counts input by the user
customer_numbers = []

#loop 7 times as per assignment criteria
for i in range(7):
    try:
        #convert input to int
        userInput=int(input(f"Please enter customer count for Day {i +1} "))
    except ValueError:
        print("Please only enter whole numbers")
        break
    customer_numbers.append(userInput)

print(customer_numbers)