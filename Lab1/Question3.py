# age = input(Enter your age: ) # 'Enter your age: ' should be surrounded with quotes ''around the prompt
# height = Input('Enter your height in cm: ') # 'Input' is the wrong function name, it should be input() 
# weight = input('Enter your weight in kg: ')  
# print(f'I am {Age} years old, {height} cm tall and weigh {Weight} kg') # The variable names are wrong, Python is case-sensitive. 'Age' and 'Weight' are the wrong variable names.

age = input('Enter your age: ')
height = float(input('Enter your height in cm: ')) * 0.0328084
weight = input('Enter your weight in kg: ')
print(f'I am {age} years old, {height:.2f} feet tall and weigh {weight} kg')
