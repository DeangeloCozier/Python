# Predictions (a): 
# The first print displays the first two elements in the array, [6.55, 6.56] excluding the [2] element. 
# The second print displays the third element from the right to the end of the list, [5.29, 5.57, 5.98] would be displayed.

#  Original Code: 
#   interest_rates = [6.55, 6.56, 5.29, 5.57, 5.98]
#   print(interest_rates[0:2])
#   print(interest_rates[-3:])

# Actual output: [6.55, 6.56]
#                [5.29, 5.57, 5.98]


# Prints the first three and last two (b):
interest_rates = [6.55, 6.56, 5.29, 5.57, 5.98]
print(interest_rates[0:3])
print(interest_rates[-2:])

# Question c:
# The original slice [0:2] does not display three rates because before the colon shows where to start and is inluded 
# but the index after the colon is excluded. Hence index 0 and 1 are printed and index 2 is excluded based on how the 
# slice works.


