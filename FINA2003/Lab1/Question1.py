# my_name = 'alex brown # (Mising Termination Quote) The string is not terminated by ' as it is left out.
# print(my_name.Lower()) # (Case-Sensitive) The lower method is using the uppercase L instead of the lowercase l (.lower()) so it wont use the right function.
# print(my_name.uppercase()) # (Wrong Function) the method is called .upper not .uppercase, this is calling a function that does not exist.
# print(myname.title()) # (Wrong Variable Name) The wrong variable name is used, a variable that does not exist(not defined), it should be my_name.

my_name = 'Deangelo Cozier'
print(my_name.lower())
print(my_name.upper())
print(my_name.title())

numberOfVowels = my_name.lower().count("a") + my_name.lower().count("e") + my_name.lower().count("i") + my_name.lower().count("o") + my_name.lower().count("u")
print (numberOfVowels)

