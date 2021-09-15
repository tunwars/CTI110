# CTI 110
# P1T2 - Salary Calculator
# Name
# Date

# Start

# Input the hours worked 
hoursWorked = input("How many hours did you work this week? ")
hoursWorked = int(hoursWorked) # convert ot integer

# Input the  hourly pay rate
hourlyPay = int(input("What's your hourly pay rate? ")) # get and convert

# Calculate gross pay (hours worked times pay rate)
grosspay = hoursWorked * hourlyPay

# Display the gross pay
print("your gross pay for the week is: $", grosspay)

# End
