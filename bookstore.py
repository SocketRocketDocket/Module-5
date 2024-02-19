#Prompt user to input number of books purchased this month
books = int(input("Enter number of books you have purchase this month: "))

#Branching to handle different ranges of input
if books < 2 and books >= 0:
    print('You have earned 0 points.')
elif 2 <= books < 4:
    print('You have earned 5 points.')
elif 4 <= books < 6:
    print('You have earned 15 points.')
elif 6 <= books < 8:
    print('You have earned 30 points.')
elif books >= 8:
    print('You have earned 60 points.')
else:
    print('Invalid input.')
