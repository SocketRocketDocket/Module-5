#Prompt the user to enter the number of years
years = int(input("Enter the number of years for average: "))

#Variables
total_months = 0
total_rainfall = 0.0

#loop to iterate through each year
for year in range(1, years + 1):
    print(f"Year {year}")
    #loop iterates through months
    for month in range(1, 13):
        #Prompt the user to enter the rainfall for the current month
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        #Add the current month's rainfall to the total
        total_rainfall += rainfall
        #Increment month
        total_months += 1

#Calculate average
average_rainfall = total_rainfall / total_months

#Output total months, total rainfall, and average monthly rainfall
print(f"\nNumber of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.3f} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")