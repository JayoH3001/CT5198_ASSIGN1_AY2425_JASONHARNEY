# Name - Jason Harney
# ID - 12461932

#init list called 'customer_numbers' that stores the customer counts input by the user
customer_numbers = []

#loop 7 times as per assignment criteria
for i in range(7):
    try:
        #convert input to int
        userInput=int(input("Please enter customer count for Day " + str(i + 1) + ": "))

        if userInput < 0:  # Prevent negative customer counts
            print("Customer count cannot be negative. Please restart the program..")
            break #exits program

        #add inputs to list
        customer_numbers.append(userInput)
        
    #check for correct input
    except ValueError:
        print("Invalid Input. Please only enter whole numbers. Please restart the program.")
        break

if len(customer_numbers) == 7:
    #total over 7 days
    customer_count_7days = sum(customer_numbers)
    print("Total Number of Customers for 7 Days: ", customer_count_7days)

    #avg over 7 days - rounded to next lower whole number as humans can't be counted with decimals
    print("Average number of customers per day: ", int(customer_count_7days / len(customer_numbers)))

    #max number
    print("Maximum customer count: ", max(customer_numbers))

    #min number
    print("Minimum customer count: ", min(customer_numbers))

    #print list per day
    #print("List of customer counts per day: ",customer_numbers)
    print("Customer count by day: ")
    for day, count in enumerate(customer_numbers, start=1):
        print("Day", day,": ", count, "customers")
