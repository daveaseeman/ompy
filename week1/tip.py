# Tip Calculator
# How much was your total bill?
# Suggest 15%, 18%, 20%
# Has to accept dollars and cents
# challenge: put in amount with or without dollar sign

# Assumptions:
# only bill input characters are real numbers, a decimel, and a dollar sign...
# only split_num input characters are whole numbers

# Get input of bill and split number from user
bill = input("How much was your total bill?\nPlease enter numbers only.\n")
split_num = input("How many people are you splitting with?\nEnter 1 if its just you.\n")

# Determine how to modify the input

# if '$' in bill: # if dollar sign present
#     bill.replace("$","") # then remove dollar sign
# left this out because inputting a $ throws an error anyway... not sure why.

gratuity = [15,
            18,
            20,
            25]

bill = float(bill) # make the remaining number a float

split = bill / split_num # split the bill

tip = [x*split/100 for x in gratuity]

extra = bill % split_num # remainder if not split evenly

print("Gratuity \t Amount/ea")
for g,t in zip(gratuity, tip):
    print("%.0f%% \t\t $%.2f" % (g,t))
